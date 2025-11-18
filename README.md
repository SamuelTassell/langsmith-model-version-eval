# LangSmith Model Version Evaluation

A Python notebook project for running evaluations on datasets to compare two AI models/providers in terms of correctness and latency using LangSmith.

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- API keys for LangSmith and OpenAI (or other model providers)

### Installation

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone https://github.com/SamuelTassell/langsmith-model-version-eval.git
   cd langsmith-model-version-eval
   ```

2. **Create a virtual environment**:
   ```bash
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate

   # On Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   ```bash
   # Copy the example environment file
   cp .env.example .env
   
   # Edit .env with your actual API keys
   # You can use nano, vim, or any text editor
   nano .env
   ```

   Required API keys:
   - `LANGCHAIN_API_KEY`: Your LangSmith API key (get it from [LangSmith](https://smith.langchain.com/))
   - `OPENAI_API_KEY`: Your OpenAI API key (get it from [OpenAI](https://platform.openai.com/))

5. **Launch Jupyter Notebook**:
   ```bash
   jupyter notebook
   ```
   
   Or use JupyterLab for a more modern interface:
   ```bash
   jupyter lab
   ```

6. **Open and run the example notebook**:
   - Navigate to `notebooks/model_evaluation.ipynb`
   - Run the cells sequentially to see the evaluation in action

## 📁 Project Structure

```
langsmith-model-version-eval/
├── notebooks/              # Jupyter notebooks for analysis
│   └── model_evaluation.ipynb  # Main evaluation notebook
├── src/                   # Python source code
│   ├── __init__.py       # Package initialization
│   ├── config.py         # Configuration management
│   ├── evaluators.py     # Custom evaluation functions
│   └── utils.py          # Utility functions
├── data/                  # Data storage (gitignored)
│   └── .gitkeep
├── .env.example          # Example environment variables
├── .gitignore            # Git ignore rules
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## 🔧 Usage

### Basic Evaluation Workflow

1. **Configure your models** in the notebook:
   ```python
   model_1 = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
   model_2 = ChatOpenAI(model="gpt-4", temperature=0.7)
   ```

2. **Prepare your test dataset**:
   - Use the example dataset provided in the notebook
   - Or load your own dataset from LangSmith
   - Or create a custom dataset

3. **Run the evaluation**:
   - Execute all cells in the notebook
   - The evaluation will measure both correctness and latency
   - Results will be visualized and exported to CSV

4. **Analyze results**:
   - Review the generated charts comparing both models
   - Check the detailed results DataFrame
   - Export results for further analysis

### Custom Evaluations

You can customize the evaluation by modifying the evaluator functions in `src/evaluators.py`:

```python
from src.evaluators import combined_evaluator

# Use custom evaluation
result = combined_evaluator(
    output=model_output,
    expected=expected_output,
    latency=response_time,
    latency_threshold=3.0  # Custom threshold
)
```

## 📊 Features

- ✅ **Easy Setup**: Simple virtual environment and dependency management
- ✅ **Model Comparison**: Compare any two models or providers
- ✅ **Dual Metrics**: Evaluate both correctness and latency
- ✅ **Visualization**: Automatic chart generation for results
- ✅ **Export**: Save results to CSV for further analysis
- ✅ **Extensible**: Easy to add custom evaluators and metrics
- ✅ **LangSmith Integration**: Built-in support for LangSmith datasets and tracing

## 🛠️ Development

### Adding New Dependencies

1. Install the package:
   ```bash
   pip install package-name
   ```

2. Update requirements.txt:
   ```bash
   pip freeze > requirements.txt
   ```

### Creating New Notebooks

1. Create a new notebook in the `notebooks/` directory
2. Import utilities from the `src/` package:
   ```python
   import sys
   sys.path.append('../src')
   from src.utils import measure_latency
   ```

## 🔐 Security

- **Never commit your `.env` file** - it contains sensitive API keys
- The `.env` file is already included in `.gitignore`
- Use `.env.example` as a template for required variables
- Rotate your API keys regularly

## 📝 Requirements

See `requirements.txt` for a complete list of dependencies. Key packages include:

- **jupyter**: Notebook interface
- **langsmith**: LangSmith Python SDK
- **langchain**: LangChain framework
- **pandas**: Data manipulation
- **matplotlib/seaborn**: Visualization
- **openai**: OpenAI API client

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🙋 Support

For questions or issues:
- Open an issue on GitHub
- Check the [LangSmith documentation](https://docs.smith.langchain.com/)
- Review the [LangChain documentation](https://python.langchain.com/)

## 🎯 Next Steps

After setting up the project:

1. **Customize the evaluation**: Modify evaluator functions for your use case
2. **Add more models**: Compare additional AI models or providers
3. **Load real data**: Connect to your LangSmith datasets
4. **Automate**: Set up scheduled evaluations
5. **Extend metrics**: Add custom evaluation criteria
