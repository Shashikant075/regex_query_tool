from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import RegexQueryForm
import re
import csv
from django.http import HttpResponse
from xhtml2pdf import pisa
from io import BytesIO
from django.template.loader import get_template
import fitz  # PyMuPDF
from django.views.decorators.csrf import csrf_exempt

def extract_text_from_pdf(file):
    """ Extract text from a PDF file """
    pdf_document = fitz.open(stream=file.read(), filetype='pdf')
    text = ''
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
    return text

@csrf_exempt
def regex_query(request):
    form = RegexQueryForm()
    matches = None

    if request.method == 'POST':
        form = RegexQueryForm(request.POST, request.FILES)
        if form.is_valid():
            text = form.cleaned_data['text']
            pattern = form.cleaned_data['pattern']
            uploaded_file = request.FILES.get('upload_file')

            try:
                if text:
                    matches = re.findall(pattern, text)
                if uploaded_file:
                    if uploaded_file.name.endswith('.pdf'):
                        uploaded_text = extract_text_from_pdf(uploaded_file)
                    else:
                        uploaded_text = uploaded_file.read().decode('utf-8')
                    matches = re.findall(pattern, uploaded_text)
            except re.error as e:
                form.add_error('pattern', f"Invalid regex pattern: {e}")

            # Store matches in the session
            request.session['matches'] = matches if matches else []
            
            # Clear the form data after processing (Line 24)
            form = RegexQueryForm()  # Reset form instance (Line 25)

    else:
        # Clear matches from the session on GET request (Line 28)
        request.session.pop('matches', None)
    
    return render(request, 'regex_query/regex_query.html', {'form': form, 'matches': matches})

def render_to_pdf(template_src, context_dict={}):
    """ Render HTML to PDF """
    template = get_template(template_src)
    html = template.render(context_dict)  # Use context_dict directly
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def download_pdf(request):
    # Fetch stored matches from session
    matches = request.session.get('matches', [])
    
    # Handle case where matches is None
    if matches is None:
        matches = []

    # Handle case where matches is empty
    if not matches:
        matches = ["No matches found."]

    # Generate PDF response
    context = {
        'matches': matches,
    }
    return render_to_pdf('regex_query/pdf_template.html', context)

def download_csv(request):
    # Generate CSV response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="matches.csv"'

    writer = csv.writer(response)
    writer.writerow(['Match'])  # Header for the CSV file

    # Fetch matches from session
    matches = request.session.get('matches', [])
    
    if matches is None:
        matches = []

    # Handle case where matches is empty
    if not matches:
        writer.writerow(['No matches found.'])
    else:
        # Write the matches from uploaded text
        for match in matches:
            writer.writerow([match])

    return response
