# regex_query_tool

The Regex Query Tool is designed to facilitate efficient searching and filtering of text and database entries using regular expressions. This tool enhances data retrieval processes by allowing complex search patterns, thus improving the ease and accuracy of finding specific information.

## Features

- **Text to Search**: Input text to perform searches within a provided text or dataset using regular expressions, allowing for advanced and flexible text searching capabilities.
  
- **Search in Upload File (optional):**: Execute regex searches directly within a Upload File (optional):, enabling efficient querying and retrieval of records that match specific patterns.

- **Regex Pattern**: Define and utilize custom regular expressions to tailor searches according to specific needs, providing powerful and precise search functionality.
## Using Regex Query Tool
- **Choose Your Search Source**: Decide whether to search within provided text or connect Upload File (optional).
- **Enter Text or Upload File (optional):**: For text search, paste the text directly into the tool. For Upload File , follow the provided instructions to configure the connection.
- **Define Your RegEx Pattern**: Construct your RegEx pattern using the supported syntax. (Documentation for RegEx syntax will be provided)
- **Run the Search**: Initiate the search process. The tool will efficiently scan the text or database and display any matches based on your RegEx pattern.
## Benefits
- **Powerful Search Capabilities**: RegEx offers unmatched flexibility and precision when searching for complex patterns in text or databases.
- **Improved Efficiency**: Quickly locate the information you need, eliminating the need for manual sifting through large datasets.
- **Enhanced Data Analysis**: Extract valuable insights from text data by identifying specific patterns and trends.

## Screenshots

<img width="469" alt="Screenshot 2024-07-18 231354" src="https://github.com/user-attachments/assets/8ddee0f8-7a43-425e-af00-cdad016466d7">



## Run Locally

To set up the Regex Query Tool, follow these steps:

1. Clone the repository to your local machine.

```bash
git clone git clone https://github.com/Shashikanttt/Regex-Query-Tool.git
```

2. Go to the project directory

```bash
cd Regex_Query_Tool
```

3. Create a Virtual Environment

```bash
py -m venv venv  # install virtual environment
venv\scripts\activate  # activate virtual environment venv
```

4. Install required packages

```bash
pip install -r requirements.txt  # install required packages
py manage.py migrate  # run first migration
```

5. Start the server

```bash
python manage.py runserver  # run the server
```

## Usage

To use the Regex Query Tool, follow these steps:

1. Access the system via the provided URL (e.g., http://127.0.0.1:8000/).

```bash
http://127.0.0.1:8000/
```

2. Input text to search or choose to search within the database using the specified regex pattern.
   search regex patterns as needed to refine search capabilities and achieve precise results.
