# FinVision

# 📊 FinVision - AI Financial Analyst

> AI-Powered Financial Analysis & Business Intelligence Platform

A comprehensive financial analysis application that extracts insights from complex financial documents, calculates key ratios, detects risks, and provides AI-driven strategic recommendations to help businesses make informed decisions.

## 🚀 Live Demo
Check out the live app here 👉 [FinVision on Streamlit](https://finvision-g.streamlit.app/)


---

## ✨ Features

### 📄 Smart Document Processing
- **PDF Extraction**: Automatically extract financial data from annual reports and statements
- **Intelligent Parsing**: AI-powered keyword recognition for financial metrics
- **Multi-Page Support**: Handle reports up to 200 pages
- **Progress Tracking**: Real-time extraction progress indicators

### 🤖 AI-Powered Analysis
- **Automated Data Extraction**: Identify revenue, profit, assets, liabilities, and equity
- **Smart Ratio Calculation**: 15+ key financial metrics computed automatically
- **Risk Detection**: Real-time identification of financial red flags
- **Strategic Recommendations**: AI-generated actionable insights with projected impact

### 📊 Comprehensive Financial Metrics
- **Profitability Analysis**: 
  - Profit Margin
  - Return on Equity (ROE)
  - Asset Turnover Ratio
- **Liquidity Indicators**:
  - Current Ratio
  - Quick Ratio
- **Leverage Metrics**:
  - Debt-to-Equity Ratio
- **Color-Coded Insights**: Visual signals for quick decision-making

### 🚨 Risk Assessment Dashboard
- **Red Flag Detection**: Automated identification of financial vulnerabilities
- **Severity Classification**: Critical, moderate, and low-priority issues
- **Benchmarking**: Compare metrics against industry standards
- **Detailed Explanations**: Clear descriptions of each risk factor

### 💡 Strategic Recommendations
- **Data-Driven Insights**: AI-generated strategic action items
- **Prioritized Actions**: Numbered recommendations by impact
- **Implementation Guidance**: Specific steps with projected outcomes
- **Cost-Benefit Analysis**: Target metrics and expected improvements

### 📥 Export & Reporting
- **PDF Reports**: Complete financial analysis with all metrics and insights
- **CSV Export**: Downloadable data for further analysis
- **JSON Format**: Structured data for integration with other tools
- **Professional Formatting**: Clean, branded report templates

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager
- (Optional) Gemini API key for enhanced AI features

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Brijesh1656/FinVision.git
cd FinVision
```

2. **Install required packages**
```bash
pip install -r requirements.txt
```

3. **Setup environment variables** (Optional)
```bash
# Create .env file in the root directory
echo "GEMINI_API_KEY=your_api_key_here" > .env
```

### Running the Application

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

---

## 📖 Usage Guide

### 1. Upload Financial Document
- Drag and drop a PDF financial statement or annual report
- Supported formats: PDF files up to 200 pages
- Automatic text extraction with progress indicator

### 2. Enter Company Details
- Input company name (e.g., "TechCorp Inc.")
- Specify fiscal year (e.g., "2024")
- Click "🚀 ANALYZE NOW" to start processing

### 3. Review Overall Health Score
- View comprehensive financial health score (0-100)
- Get instant grade: Excellent (80+), Good (60-79), Fair (40-59), Poor (<40)
- Understand overall financial position at a glance

### 4. Explore Detailed Analysis
- **Overview Tab**: Key performance indicators with progress bars
- **Detailed Metrics Tab**: In-depth ratio analysis with benchmarks
- **Risk Analysis Tab**: Identified red flags and concerns
- **Recommendations Tab**: AI-generated strategic action items

### 5. Export Analysis
- Download complete report in PDF format
- Export metrics to CSV for spreadsheet analysis
- Get JSON data for integration with other tools

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Streamlit** | Web application framework |
| **PyPDF2** | PDF text extraction and processing |
| **Pandas** | Data manipulation and analysis |
| **Python-dotenv** | Environment variable management |
| **Google Gemini API** | AI-powered insights (optional) |
| **OpenAI/LangChain** | Enhanced AI analysis capabilities |
| **Custom CSS/HTML** | Premium glassmorphic UI design |

---

## 📊 Analyzed Financial Ratios

### Profitability Metrics
- **Profit Margin**: Revenue converted to profit | Excellent: >15%
- **Return on Equity (ROE)**: Shareholder investment returns | Excellent: >20%
- **Asset Turnover**: Revenue generation efficiency | Excellent: >1.5

### Liquidity Indicators
- **Current Ratio**: Short-term obligation coverage | Excellent: >2.0
- **Quick Ratio**: Immediate liquidity test | Excellent: >1.5

### Leverage Analysis
- **Debt-to-Equity**: Financial leverage assessment | Excellent: <0.5

---

## 🎯 Use Cases

- **Investment Analysis**: Evaluate company health before investing
- **Due Diligence**: Quick financial assessment for M&A activities
- **Credit Risk Assessment**: Analyze borrower financial stability
- **Financial Consulting**: Generate professional client reports efficiently
- **Academic Research**: Study financial patterns and trends across companies
- **Internal Auditing**: Monitor organizational financial health continuously
- **Business Valuation**: Support valuation models with comprehensive data

---

## ⚠️ Disclaimer

**This application is for educational and informational purposes only.**

- Not professional financial or investment advice
- Automated extraction may vary based on document quality
- Always verify extracted data against source documents
- Consider consulting with qualified financial professionals for critical decisions

---

## 🐛 Known Issues

- PDF extraction accuracy depends on document structure and quality
- Scanned PDFs (images) may not extract text properly
- Demo data is used when no financial data is detected
- Some complex financial statements may require manual verification

---

## 📈 Roadmap

### Feature Ideas
- [ ] Support for Excel and CSV financial statements
- [ ] Multi-year comparative analysis
- [ ] Industry benchmarking and peer comparison
- [ ] Real-time market data integration
- [ ] Interactive data visualizations with charts
- [ ] OCR support for scanned documents
- [ ] Multi-language support
- [ ] API endpoint for programmatic access
- [ ] Cryptocurrency and DeFi analysis
- [ ] ESG (Environmental, Social, Governance) scoring

---

## 👨‍💻 Author

**Brijesh Singh**

- GitHub: [@Brijesh1656](https://github.com/Brijesh1656)
- LinkedIn: [brijesh-singh-b84275307](https://linkedin.com/in/brijesh-singh-b84275307)
- Email: brijesh7146@gmail.com
- Location: Hyderabad, India

### About Me
BBA (Business Analytics) student passionate about leveraging data and machine learning to deliver business insights. Experienced in Python, SQL, Power BI, and building full-stack data applications.

---

## 🎓 Related Projects

Check out my other data science projects:
- **[Stock Analysis Pro](https://github.com/Brijesh1656/Stock-Analysis-Pro)** - AI-powered stock analysis with technical indicators and backtesting
- **Personal Chatbot** - Interactive chatbot using Google Gemini API with NLP capabilities

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Streamlit community for the amazing framework
- Google Gemini API for AI capabilities
- OpenAI and LangChain for enhanced NLP features
- All contributors and users providing valuable feedback

---

## 📞 Support

For support, email brijesh7146@gmail.com or open an issue in the GitHub repository.

---

<div align="center">

**⭐ Star this repo if you find it helpful!**

Made with ❤️ and ☕ by Brijesh Singh

</div>
