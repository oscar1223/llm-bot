# LangChain AI Bots Collection

A collection of specialized bots developed using the **LangChain** framework and various AI models to perform different tasks related to natural language processing, document analysis, and specialized knowledge domains.

## 🤖 Projects

### 📄 ChatPDF
A document analysis bot that can:
- Process and analyze PDF documents
- Answer specific questions about the documents
- Generate complete or chapter-based summaries
- Provide page references for information sources

**Implementation**: Uses LangChain's document loading, text splitting, embeddings, and retrieval QA chains to create a conversational interface for PDF documents.

**Files**: 
- [main.py](chatpdf/main.py) - Terminal-based chat interface
- [pdfprocessing.py](chatpdf/pdfprocessing.py) - Core PDF processing functionality

### 🩺 DoctorBot
A medical consultation bot that:
- Connects to reliable medical websites
- Answers health-related questions
- Provides advice on various diseases and ailments
- Uses a compassionate medical professional tone

**Implementation**: Uses a custom LangChain agent with DuckDuckGo search tools specifically targeted at medical websites to provide reliable health information.

**Files**:
- [Doctorbot.py](Doctorbot/Doctorbot.py) - Complete implementation with custom agent, tools, and memory

### 🔄 SQLConverter
A tool that:
- Converts SQL procedures and statements to Python scripts
- Performs database operations through conversational interfaces
- Translates database logic between languages

**Implementation**: Uses LangChain agents to analyze SQL code and generate equivalent Python implementations.

**Files**:
- [SQLconverter.py](SQLconverter/SQLconverter.py) - SQL to Python conversion functionality
- [llmsql.py](SQLconverter/llmsql.py) - Natural language to SQL database agent

### 🖼️ LLM-OCR (Under Development)
A planned image-to-text processing bot that will:
- Extract text from images using OCR technology
- Process the extracted text using AI models
- Enable AI text analysis on image-based content

**Implementation**: Combines image processing techniques with LangChain's text analysis capabilities.

**Files**:
- [image_processor.py](llm-ocr/image_processor.py) - Image preprocessing and OCR functionality

### 📝 LangChain Notes
A collection of examples and exercises demonstrating various LangChain features:
- Different types of chains (Sequential, Router)
- Agent implementations
- Prompt engineering techniques
- Memory implementations

**Files**:
- [chains.py](langchain%20notes/chains.py) - Examples of various LangChain chain implementations

## 🚀 Getting Started

1. Clone this repository
2. Install the requirements for the specific project you want to use
3. Create a `.env` file with your OpenAI API key:
4. Run the specific project script

## ⚙️ Requirements

Each project has its own specific requirements, but common dependencies include:
- Python 3.8+
- LangChain
- OpenAI API access
- Specific libraries depending on the project (see individual project files)

## 📜 License
[Apache 2.0](https://choosealicense.com/licenses/apache-2.0/)

