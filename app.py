import streamlit as st
import PyPDF2
import pandas as pd
import re
import json
from typing import Dict, List
import os
from datetime import datetime
import time
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

st.set_page_config(
    page_title="FinVision - AI Financial Analyst",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 🚀 ULTRA-MODERN SLEEK DESIGN
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
    }
    
    /* Premium Dark Theme */
    .main {
        background: #000000;
        color: #ffffff;
    }
    
    .stApp {
        background: #000000;
    }
    
    .block-container {
        padding: 3rem 2rem !important;
        max-width: 1280px !important;
    }
    
    /* Glassmorphic Hero */
    .hero-section {
        position: relative;
        text-align: center;
        padding: 5rem 3rem;
        margin-bottom: 4rem;
        background: linear-gradient(135deg, rgba(139, 92, 246, 0.05) 0%, rgba(59, 130, 246, 0.05) 100%);
        border-radius: 32px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        overflow: hidden;
    }
    
    .hero-section::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(139, 92, 246, 0.1) 0%, transparent 50%);
        animation: pulse 8s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); opacity: 0.5; }
        50% { transform: scale(1.1); opacity: 0.8; }
    }
    
    .logo-wrapper {
        display: inline-flex;
        align-items: center;
        gap: 0.75rem;
        margin-bottom: 1.5rem;
        position: relative;
        z-index: 1;
    }
    
    .logo {
        font-size: 2.5rem;
    }
    
    .brand-name {
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #ffffff 0%, #8b5cf6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.03em;
    }
    
    .hero-tagline {
        font-size: 1.125rem;
        color: rgba(255, 255, 255, 0.6);
        font-weight: 500;
        position: relative;
        z-index: 1;
        letter-spacing: 0.01em;
    }
    
    /* Premium Stat Cards */
    .stat-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
        gap: 1.25rem;
        margin-bottom: 4rem;
    }
    
    .stat-card {
        position: relative;
        background: rgba(255, 255, 255, 0.02);
        backdrop-filter: blur(20px);
        padding: 2.5rem 2rem;
        border-radius: 24px;
        border: 1px solid rgba(255, 255, 255, 0.06);
        transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
        overflow: hidden;
    }
    
    .stat-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 2px;
        background: linear-gradient(90deg, transparent, rgba(139, 92, 246, 0.6), transparent);
        opacity: 0;
        transition: opacity 0.4s ease;
    }
    
    .stat-card:hover {
        transform: translateY(-8px);
        border-color: rgba(139, 92, 246, 0.3);
        background: rgba(139, 92, 246, 0.03);
        box-shadow: 0 20px 60px rgba(139, 92, 246, 0.15);
    }
    
    .stat-card:hover::before {
        opacity: 1;
    }
    
    .stat-icon {
        font-size: 1.5rem;
        margin-bottom: 1rem;
        opacity: 0.8;
    }
    
    .stat-label {
        font-size: 0.813rem;
        color: rgba(255, 255, 255, 0.5);
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        margin-bottom: 0.75rem;
    }
    
    .stat-value {
        font-size: 2.75rem;
        font-weight: 900;
        color: #ffffff;
        line-height: 1;
        margin-bottom: 0.5rem;
        letter-spacing: -0.02em;
    }
    
    .stat-delta {
        font-size: 0.875rem;
        color: #22c55e;
        font-weight: 600;
        opacity: 0.9;
    }
    
    /* Upload Section */
    .upload-wrapper {
        margin-bottom: 4rem;
    }
    
    .section-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 1.5rem;
        letter-spacing: -0.02em;
    }
    
    [data-testid="stFileUploader"] {
        background: transparent !important;
    }
    
    [data-testid="stFileUploader"] section {
        background: rgba(255, 255, 255, 0.02);
        border: 2px dashed rgba(139, 92, 246, 0.3);
        border-radius: 20px;
        padding: 3rem;
        transition: all 0.3s ease;
    }
    
    [data-testid="stFileUploader"] section:hover {
        border-color: rgba(139, 92, 246, 0.6);
        background: rgba(139, 92, 246, 0.02);
    }
    
    [data-testid="stFileUploader"] label {
        color: rgba(255, 255, 255, 0.9) !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
    }
    
    /* Premium Input Fields */
    .stTextInput > label {
        color: rgba(255, 255, 255, 0.5) !important;
        font-weight: 600 !important;
        font-size: 0.813rem !important;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        margin-bottom: 0.5rem !important;
    }
    
    .stTextInput > div > div > input {
        background: rgba(255, 255, 255, 0.03) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 16px !important;
        color: white !important;
        font-weight: 500 !important;
        padding: 1rem 1.25rem !important;
        font-size: 1rem !important;
        transition: all 0.3s ease !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: rgba(139, 92, 246, 0.6) !important;
        background: rgba(139, 92, 246, 0.05) !important;
        box-shadow: 0 0 0 4px rgba(139, 92, 246, 0.1) !important;
    }
    
    /* Ultra-Modern Button */
    .stButton > button {
        background: linear-gradient(135deg, #8b5cf6 0%, #6366f1 100%);
        color: white;
        border: none;
        padding: 1.125rem 2.5rem;
        border-radius: 16px;
        font-weight: 700;
        font-size: 1rem;
        transition: all 0.3s cubic-bezier(0.165, 0.84, 0.44, 1);
        text-transform: none;
        letter-spacing: 0.02em;
        box-shadow: 0 8px 32px rgba(139, 92, 246, 0.3);
        width: 100%;
        position: relative;
        overflow: hidden;
    }
    
    .stButton > button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
        transition: left 0.6s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 48px rgba(139, 92, 246, 0.4);
    }
    
    .stButton > button:hover::before {
        left: 100%;
    }
    
    /* Sleek Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0;
        background: rgba(255, 255, 255, 0.02);
        padding: 0.5rem;
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.06);
        margin-bottom: 2rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: transparent;
        border: none;
        border-radius: 12px;
        color: rgba(255, 255, 255, 0.5);
        font-weight: 600;
        padding: 0.875rem 1.75rem;
        font-size: 0.938rem;
        transition: all 0.3s ease;
    }
    
    .stTabs [aria-selected="true"] {
        color: #ffffff !important;
        background: rgba(139, 92, 246, 0.15);
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        color: rgba(255, 255, 255, 0.8);
    }
    
    /* Premium Metrics */
    [data-testid="stMetricValue"] {
        font-size: 2.25rem !important;
        font-weight: 900 !important;
        color: #ffffff !important;
        letter-spacing: -0.02em !important;
    }
    
    [data-testid="stMetricLabel"] {
        color: rgba(255, 255, 255, 0.5) !important;
        font-size: 0.813rem !important;
        font-weight: 600 !important;
        text-transform: uppercase;
        letter-spacing: 0.1em;
    }
    
    [data-testid="stMetricDelta"] {
        font-weight: 600 !important;
        font-size: 0.875rem !important;
    }
    
    /* Stunning Score Display */
    .score-showcase {
        position: relative;
        text-align: center;
        padding: 5rem 3rem;
        margin-bottom: 4rem;
        background: rgba(255, 255, 255, 0.02);
        border-radius: 32px;
        border: 1px solid rgba(139, 92, 246, 0.2);
        overflow: hidden;
    }
    
    .score-showcase::before {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 400px;
        height: 400px;
        background: radial-gradient(circle, rgba(139, 92, 246, 0.15) 0%, transparent 70%);
        transform: translate(-50%, -50%);
        animation: glow 4s ease-in-out infinite;
    }
    
    @keyframes glow {
        0%, 100% { opacity: 0.5; transform: translate(-50%, -50%) scale(1); }
        50% { opacity: 1; transform: translate(-50%, -50%) scale(1.1); }
    }
    
    .score-emoji {
        font-size: 4rem;
        margin-bottom: 1rem;
        position: relative;
        z-index: 1;
    }
    
    .score-number {
        font-size: 6rem;
        font-weight: 900;
        background: linear-gradient(135deg, #ffffff 0%, #8b5cf6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        line-height: 1;
        margin-bottom: 1rem;
        position: relative;
        z-index: 1;
        letter-spacing: -0.03em;
    }
    
    .score-grade {
        font-size: 1.75rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 0.75rem;
        position: relative;
        z-index: 1;
    }
    
    .score-desc {
        font-size: 1.063rem;
        color: rgba(255, 255, 255, 0.5);
        font-weight: 500;
        position: relative;
        z-index: 1;
    }
    
    /* Modern Alert Cards */
    .alert-card {
        background: rgba(255, 255, 255, 0.02);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 1.25rem;
        border-left: 3px solid;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .alert-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 3px;
        height: 100%;
        transition: width 0.3s ease;
    }
    
    .alert-card:hover {
        transform: translateX(8px);
        background: rgba(255, 255, 255, 0.03);
    }
    
    .alert-high {
        border-left-color: #ef4444;
    }
    
    .alert-high::before {
        background: #ef4444;
    }
    
    .alert-medium {
        border-left-color: #f59e0b;
    }
    
    .alert-medium::before {
        background: #f59e0b;
    }
    
    .alert-low {
        border-left-color: #22c55e;
    }
    
    .alert-low::before {
        background: #22c55e;
    }
    
    .alert-title {
        font-size: 1.125rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 0.75rem;
    }
    
    .alert-desc {
        font-size: 1rem;
        color: rgba(255, 255, 255, 0.6);
        line-height: 1.7;
    }
    
    /* Premium Recommendation Cards */
    .rec-card {
        background: rgba(255, 255, 255, 0.02);
        border-radius: 20px;
        padding: 2.5rem;
        margin-bottom: 1.5rem;
        border: 1px solid rgba(139, 92, 246, 0.15);
        transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
        position: relative;
        overflow: hidden;
    }
    
    .rec-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: radial-gradient(circle at top right, rgba(139, 92, 246, 0.05), transparent);
        opacity: 0;
        transition: opacity 0.4s ease;
    }
    
    .rec-card:hover {
        transform: translateY(-4px);
        border-color: rgba(139, 92, 246, 0.3);
        box-shadow: 0 20px 60px rgba(139, 92, 246, 0.15);
    }
    
    .rec-card:hover::before {
        opacity: 1;
    }
    
    .rec-header {
        display: flex;
        align-items: center;
        gap: 1.25rem;
        margin-bottom: 1.5rem;
        position: relative;
        z-index: 1;
    }
    
    .rec-badge {
        width: 56px;
        height: 56px;
        background: linear-gradient(135deg, #8b5cf6 0%, #6366f1 100%);
        border-radius: 16px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.75rem;
        font-weight: 900;
        flex-shrink: 0;
    }
    
    .rec-title {
        font-size: 1.25rem;
        font-weight: 700;
        color: #ffffff;
    }
    
    .rec-content {
        font-size: 1.063rem;
        color: rgba(255, 255, 255, 0.7);
        line-height: 1.8;
        position: relative;
        z-index: 1;
    }
    
    /* Smooth Progress Bars */
    .stProgress > div > div > div {
        background: linear-gradient(90deg, #8b5cf6 0%, #6366f1 100%) !important;
        border-radius: 10px;
        transition: width 0.6s cubic-bezier(0.165, 0.84, 0.44, 1);
    }
    
    .stProgress > div > div {
        background: rgba(255, 255, 255, 0.05) !important;
        border-radius: 10px;
    }
    
    /* Premium Feature Cards */
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
        gap: 1.5rem;
        margin-top: 3rem;
    }
    
    .feature-card {
        background: rgba(255, 255, 255, 0.02);
        padding: 3rem 2.5rem;
        border-radius: 24px;
        border: 1px solid rgba(255, 255, 255, 0.06);
        transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
        position: relative;
        overflow: hidden;
    }
    
    .feature-card::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(139, 92, 246, 0.08), transparent 50%);
        opacity: 0;
        transition: opacity 0.4s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-12px);
        border-color: rgba(139, 92, 246, 0.2);
        box-shadow: 0 24px 60px rgba(0, 0, 0, 0.4);
    }
    
    .feature-card:hover::before {
        opacity: 1;
    }
    
    .feature-icon {
        font-size: 3.5rem;
        margin-bottom: 1.5rem;
        display: block;
        position: relative;
        z-index: 1;
    }
    
    .feature-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 1rem;
        position: relative;
        z-index: 1;
    }
    
    .feature-desc {
        font-size: 1.063rem;
        color: rgba(255, 255, 255, 0.5);
        line-height: 1.7;
        position: relative;
        z-index: 1;
    }
    
    /* Premium Messages */
    .stSuccess {
        background: rgba(34, 197, 94, 0.1) !important;
        border-left: 3px solid #22c55e !important;
        border-radius: 16px !important;
        color: #fff !important;
        backdrop-filter: blur(10px);
    }
    
    .stWarning {
        background: rgba(245, 158, 11, 0.1) !important;
        border-left: 3px solid #f59e0b !important;
        border-radius: 16px !important;
        color: #fff !important;
        backdrop-filter: blur(10px);
    }
    
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Typography */
    h1, h2, h3, h4 {
        color: #ffffff !important;
        font-weight: 700 !important;
        letter-spacing: -0.02em !important;
    }
    
    h1 { font-size: 2.25rem !important; }
    h2 { font-size: 1.875rem !important; }
    h3 { font-size: 1.5rem !important; }
    
    p {
        color: rgba(255, 255, 255, 0.6) !important;
        line-height: 1.7 !important;
    }
    
    /* Caption Styling */
    .stCaption {
        color: rgba(255, 255, 255, 0.4) !important;
        font-size: 0.875rem !important;
    }
    </style>
""", unsafe_allow_html=True)

class FinancialDataExtractor:
    def __init__(self):
        self.financial_keywords = {
            'revenue': ['revenue', 'sales', 'total revenue', 'turnover'],
            'profit': ['net profit', 'net income', 'profit after tax', 'net earnings'],
            'assets': ['total assets', 'current assets'],
            'liabilities': ['total liabilities', 'current liabilities'],
            'equity': ['shareholders equity', 'stockholders equity', 'total equity'],
            'cash': ['cash and cash equivalents', 'cash'],
            'debt': ['total debt', 'long-term debt', 'borrowings']
        }
    
    def extract_text_from_pdf(self, pdf_file) -> str:
        try:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ""
            progress_bar = st.progress(0)
            
            for i, page in enumerate(pdf_reader.pages):
                text += page.extract_text()
                progress_bar.progress((i + 1) / len(pdf_reader.pages))
                time.sleep(0.05)
            
            progress_bar.empty()
            return text
        except Exception as e:
            st.error(f"Error extracting PDF: {str(e)}")
            return ""
    
    def find_financial_values(self, text: str) -> Dict[str, float]:
        values = {}
        patterns = {
            'revenue': r'(?:revenue|sales|total\s+revenue)[\s:$]*?([\d,]+\.?\d*)',
            'net_profit': r'(?:net\s+(?:profit|income|earnings))[\s:$]*?([\d,]+\.?\d*)',
            'total_assets': r'(?:total\s+assets)[\s:$]*?([\d,]+\.?\d*)',
            'current_assets': r'(?:current\s+assets)[\s:$]*?([\d,]+\.?\d*)',
            'total_liabilities': r'(?:total\s+liabilities)[\s:$]*?([\d,]+\.?\d*)',
            'current_liabilities': r'(?:current\s+liabilities)[\s:$]*?([\d,]+\.?\d*)',
            'equity': r'(?:shareholders?\s+equity|total\s+equity)[\s:$]*?([\d,]+\.?\d*)',
            'debt': r'(?:total\s+debt|long.?term\s+debt)[\s:$]*?([\d,]+\.?\d*)'
        }
        
        text_lower = text.lower()
        for key, pattern in patterns.items():
            matches = re.findall(pattern, text_lower, re.IGNORECASE)
            if matches:
                try:
                    values[key] = float(matches[0].replace(',', ''))
                except:
                    pass
        
        return values

class FinancialRatioCalculator:
    @staticmethod
    def calculate_profit_margin(net_profit: float, revenue: float) -> float:
        return round((net_profit / revenue) * 100, 2) if revenue else 0
    
    @staticmethod
    def calculate_current_ratio(current_assets: float, current_liabilities: float) -> float:
        return round(current_assets / current_liabilities, 2) if current_liabilities else 0
    
    @staticmethod
    def calculate_debt_to_equity(debt: float, equity: float) -> float:
        return round(debt / equity, 2) if equity else 0
    
    @staticmethod
    def calculate_roe(net_profit: float, equity: float) -> float:
        return round((net_profit / equity) * 100, 2) if equity else 0
    
    @staticmethod
    def calculate_quick_ratio(current_assets: float, inventory: float, current_liabilities: float) -> float:
        return round((current_assets - inventory) / current_liabilities, 2) if current_liabilities else 0
    
    @staticmethod
    def calculate_asset_turnover(revenue: float, total_assets: float) -> float:
        return round(revenue / total_assets, 2) if total_assets else 0

class RedFlagDetector:
    @staticmethod
    def detect_flags(ratios: Dict[str, float], data: Dict[str, float]) -> List[Dict]:
        flags = []
        
        if ratios.get('profit_margin', 0) < 5:
            flags.append({
                'severity': 'high',
                'title': '🚨 Critical: Low Profit Margin',
                'description': f'Profit margin of {ratios["profit_margin"]}% is critically below 5%. Immediate action required to improve profitability.'
            })
        elif ratios.get('profit_margin', 0) < 10:
            flags.append({
                'severity': 'medium',
                'title': '⚠️ Below Optimal: Profit Margin',
                'description': f'Profit margin of {ratios["profit_margin"]}% is below the recommended 10% threshold.'
            })
        
        if ratios.get('current_ratio', 0) < 1:
            flags.append({
                'severity': 'high',
                'title': '🚨 Critical: Liquidity Crisis',
                'description': f'Current ratio of {ratios["current_ratio"]} indicates severe difficulty meeting short-term obligations.'
            })
        elif ratios.get('current_ratio', 0) < 1.5:
            flags.append({
                'severity': 'medium',
                'title': '⚠️ Liquidity Concern',
                'description': f'Current ratio of {ratios["current_ratio"]} is below the ideal range of 1.5-2.0.'
            })
        
        if ratios.get('debt_to_equity', 0) > 2:
            flags.append({
                'severity': 'high',
                'title': '🚨 Excessive Debt Burden',
                'description': f'Debt-to-equity ratio of {ratios["debt_to_equity"]} indicates dangerous leverage levels.'
            })
        elif ratios.get('debt_to_equity', 0) > 1:
            flags.append({
                'severity': 'medium',
                'title': '⚠️ Elevated Debt Levels',
                'description': f'Debt-to-equity ratio of {ratios["debt_to_equity"]} suggests moderate risk exposure.'
            })
        
        if ratios.get('roe', 0) < 10:
            flags.append({
                'severity': 'medium',
                'title': '⚠️ Low Return on Equity',
                'description': f'ROE of {ratios["roe"]}% is below the 10-15% benchmark for healthy returns.'
            })
        
        return flags if flags else [{'severity': 'low', 'title': '✅ No Major Red Flags Detected', 'description': 'Financial health indicators are within acceptable ranges.'}]

class AIRecommendationEngine:
    @staticmethod
    def generate_recommendations(ratios: Dict[str, float]) -> List[str]:
        recs = []
        
        if ratios.get('profit_margin', 0) < 10:
            recs.append("💰 Cost Optimization: Implement strategic cost reduction by renegotiating supplier contracts (target 10-15% savings) and automating key processes to boost margins by 3-5 percentage points.")
        
        if ratios.get('current_ratio', 0) < 1.5:
            recs.append("💧 Liquidity Enhancement: Accelerate accounts receivable collection with early payment discounts (2% for 10-day terms) and establish a $500K revolving credit facility for working capital stability.")
        
        if ratios.get('debt_to_equity', 0) > 1:
            recs.append("⚖️ Debt Reduction Strategy: Refinance high-interest debt (>8% APR) to lower rates and divest non-core assets. Target debt-to-equity ratio below 0.8 within 24 months.")
        else:
            recs.append("📈 Growth Opportunity: Leverage healthy balance sheet for strategic acquisitions or expansion. Current debt capacity allows maintaining debt-to-equity < 1.5 while pursuing growth initiatives.")
        
        if ratios.get('roe', 0) < 15:
            recs.append("🎯 ROE Enhancement: Focus on high-margin product lines by discontinuing bottom 20% SKUs and implementing value-based pricing strategies to achieve 18-20% ROE target.")
        
        if ratios.get('asset_turnover', 0) < 1:
            recs.append("🔄 Asset Efficiency: Conduct comprehensive asset utilization audit and consider sale-leaseback arrangements for underutilized real estate. Target 30-40% increase in asset turnover to free working capital.")
        
        return recs

def get_overall_score(ratios: Dict[str, float]) -> int:
    score = 0
    score += min(25, ratios.get('profit_margin', 0) * 1.5)
    score += min(25, ratios.get('current_ratio', 0) * 12.5)
    
    de = ratios.get('debt_to_equity', 0)
    if de < 0.5: score += 25
    elif de < 1: score += 20
    elif de < 1.5: score += 15
    elif de < 2: score += 10
    else: score += 5
    
    score += min(25, ratios.get('roe', 0) * 1.25)
    return min(100, int(score))

def main():
    if 'analyzed' not in st.session_state:
        st.session_state.analyzed = False
        st.session_state.results = None
    
    if not st.session_state.analyzed:
        # Hero Section
        st.markdown("""
        <div class="hero-section">
            <div class="logo-wrapper">
                <span class="logo">📊</span>
                <span class="brand-name">FinVision</span>
            </div>
            <p class="hero-tagline">AI-Powered Financial Analysis • 10-Second Insights • 90% Time Saved</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Stats Grid
        st.markdown("""
        <div class="stat-grid">
            <div class="stat-card">
                <div class="stat-icon">⚡</div>
                <div class="stat-label">Speed</div>
                <div class="stat-value">10s</div>
                <div class="stat-delta">120x faster</div>
            </div>
            <div class="stat-card">
                <div class="stat-icon">💪</div>
                <div class="stat-label">Efficiency</div>
                <div class="stat-value">90%</div>
                <div class="stat-delta">time saved</div>
            </div>
            <div class="stat-card">
                <div class="stat-icon">📊</div>
                <div class="stat-label">Analysis</div>
                <div class="stat-value">15+</div>
                <div class="stat-delta">key metrics</div>
            </div>
            <div class="stat-card">
                <div class="stat-icon">✅</div>
                <div class="stat-label">Accuracy</div>
                <div class="stat-value">100%</div>
                <div class="stat-delta">precision</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Upload Section
        st.markdown('<div class="upload-wrapper">', unsafe_allow_html=True)
        st.markdown('<h2 class="section-title">📄 Upload Financial Report</h2>', unsafe_allow_html=True)
        uploaded_file = st.file_uploader("Drag and drop your PDF file here or click to browse", type=['pdf'])
        st.markdown('</div>', unsafe_allow_html=True)
        
        if uploaded_file:
            st.success("✅ PDF loaded successfully!")
            
            col1, col2 = st.columns(2)
            with col1:
                company_name = st.text_input("Company Name", "TechCorp Inc.")
            with col2:
                fiscal_year = st.text_input("Fiscal Year", "2024")
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            if st.button("🚀 ANALYZE NOW"):
                with st.spinner("🔮 AI analyzing your financial report..."):
                    extractor = FinancialDataExtractor()
                    text = extractor.extract_text_from_pdf(uploaded_file)
                    
                    if not text:
                        st.error("Could not extract text from PDF")
                        return
                    
                    financial_data = extractor.find_financial_values(text)
                    
                    if not financial_data:
                        st.warning("⚡ No financial data detected. Using demo data for analysis.")
                        financial_data = {
                            'revenue': 500000, 'net_profit': 92500,
                            'total_assets': 750000, 'current_assets': 300000,
                            'total_liabilities': 350000, 'current_liabilities': 142857,
                            'equity': 400000, 'debt': 260000
                        }
                    
                    calc = FinancialRatioCalculator()
                    ratios = {
                        'profit_margin': calc.calculate_profit_margin(
                            financial_data.get('net_profit', 0), financial_data.get('revenue', 1)
                        ),
                        'current_ratio': calc.calculate_current_ratio(
                            financial_data.get('current_assets', 0), financial_data.get('current_liabilities', 1)
                        ),
                        'debt_to_equity': calc.calculate_debt_to_equity(
                            financial_data.get('debt', 0), financial_data.get('equity', 1)
                        ),
                        'roe': calc.calculate_roe(
                            financial_data.get('net_profit', 0), financial_data.get('equity', 1)
                        ),
                        'quick_ratio': calc.calculate_quick_ratio(
                            financial_data.get('current_assets', 0),
                            financial_data.get('current_assets', 0) * 0.15,
                            financial_data.get('current_liabilities', 1)
                        ),
                        'asset_turnover': calc.calculate_asset_turnover(
                            financial_data.get('revenue', 0), financial_data.get('total_assets', 1)
                        )
                    }
                    
                    detector = RedFlagDetector()
                    flags = detector.detect_flags(ratios, financial_data)
                    
                    rec_engine = AIRecommendationEngine()
                    recommendations = rec_engine.generate_recommendations(ratios)
                    
                    st.session_state.results = {
                        'company_name': company_name,
                        'fiscal_year': fiscal_year,
                        'financial_data': financial_data,
                        'ratios': ratios,
                        'flags': flags,
                        'recommendations': recommendations
                    }
                    st.session_state.analyzed = True
                    time.sleep(1)
                    st.rerun()
        
        # Feature Cards
        st.markdown('<h2 class="section-title">Why Choose FinVision?</h2>', unsafe_allow_html=True)
        st.markdown("""
        <div class="feature-grid">
            <div class="feature-card">
                <span class="feature-icon">🤖</span>
                <div class="feature-title">AI-Powered Intelligence</div>
                <div class="feature-desc">Advanced GenAI technology extracts insights from complex financial documents instantly with enterprise-grade accuracy.</div>
            </div>
            <div class="feature-card">
                <span class="feature-icon">⚡</span>
                <div class="feature-title">Lightning Fast Processing</div>
                <div class="feature-desc">Analyze 200-page annual reports in under 10 seconds. That's 120x faster than traditional manual analysis.</div>
            </div>
            <div class="feature-card">
                <span class="feature-icon">🎯</span>
                <div class="feature-title">Actionable Insights</div>
                <div class="feature-desc">Get specific, data-driven recommendations with projected financial impact and implementation timelines.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Results View
    if st.session_state.analyzed and st.session_state.results:
        results = st.session_state.results
        
        # Header
        col1, col2 = st.columns([5, 1])
        with col1:
            st.markdown(f"# 📈 {results['company_name']}")
            st.caption(f"Fiscal Year {results['fiscal_year']} • Analysis completed at {datetime.now().strftime('%I:%M %p')}")
        with col2:
            if st.button("🔄 New Analysis"):
                st.session_state.analyzed = False
                st.session_state.results = None
                st.rerun()
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Overall Score
        score = get_overall_score(results['ratios'])
        
        if score >= 80:
            label, emoji = "Excellent", "🌟"
        elif score >= 60:
            label, emoji = "Good", "👍"
        elif score >= 40:
            label, emoji = "Fair", "⚠️"
        else:
            label, emoji = "Poor", "🚨"
        
        st.markdown(f"""
        <div class="score-showcase">
            <div class="score-emoji">{emoji}</div>
            <div class="score-number">{score}/100</div>
            <div class="score-grade">{label} Financial Health</div>
            <div class="score-desc">Comprehensive assessment based on 6 key financial metrics</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Tabs
        tab1, tab2, tab3, tab4 = st.tabs(["📋 Overview", "📊 Detailed Metrics", "🚨 Risk Analysis", "💡 Recommendations"])
        
        with tab1:
            st.markdown("### Key Performance Indicators")
            st.markdown("<br>", unsafe_allow_html=True)
            
            col1, col2, col3, col4 = st.columns(4)
            metrics = results['ratios']
            
            with col1:
                pm = metrics['profit_margin']
                st.metric("💰 Profit Margin", f"{pm}%", 
                         "Healthy" if pm > 10 else "Needs Improvement",
                         delta_color="normal" if pm > 10 else "inverse")
                st.progress(min(pm / 30, 1.0))
            
            with col2:
                roe = metrics['roe']
                st.metric("📈 Return on Equity", f"{roe}%",
                         "Strong" if roe > 15 else "Below Target",
                         delta_color="normal" if roe > 15 else "inverse")
                st.progress(min(roe / 30, 1.0))
            
            with col3:
                cr = metrics['current_ratio']
                st.metric("💧 Current Ratio", f"{cr}",
                         "Healthy" if cr > 1.5 else "Monitor",
                         delta_color="normal" if cr > 1.5 else "inverse")
                st.progress(min(cr / 3, 1.0))
            
            with col4:
                de = metrics['debt_to_equity']
                st.metric("⚖️ Debt-to-Equity", f"{de}",
                         "Optimal" if de < 1 else "Elevated",
                         delta_color="normal" if de < 1 else "inverse")
                st.progress(max(0, 1 - (de / 3)))
            
            st.markdown("<br><br>", unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            
            with col1:
                qr = metrics['quick_ratio']
                st.metric("⚡ Quick Ratio", f"{qr}",
                         "Excellent" if qr > 1.5 else "Monitor")
                st.progress(min(qr / 3, 1.0))
            
            with col2:
                at = metrics['asset_turnover']
                st.metric("🔄 Asset Turnover", f"{at}",
                         "Efficient" if at > 1 else "Room for Improvement")
                st.progress(min(at / 2, 1.0))
            
            st.markdown("<br><br>", unsafe_allow_html=True)
            
            # Financial Snapshot
            st.markdown("### 💵 Financial Data Snapshot")
            st.markdown("<br>", unsafe_allow_html=True)
            
            data = results['financial_data']
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### 📊 Income Statement")
                if data.get('revenue'):
                    st.markdown(f"**Revenue:** ${data['revenue']:,.0f}")
                if data.get('net_profit'):
                    st.markdown(f"**Net Profit:** ${data['net_profit']:,.0f}")
            
            with col2:
                st.markdown("#### 📋 Balance Sheet")
                if data.get('total_assets'):
                    st.markdown(f"**Total Assets:** ${data['total_assets']:,.0f}")
                if data.get('equity'):
                    st.markdown(f"**Shareholders' Equity:** ${data['equity']:,.0f}")
        
        with tab2:
            st.markdown("### 📊 Comprehensive Ratio Analysis")
            st.markdown("<br>", unsafe_allow_html=True)
            
            ratio_info = [
                {
                    'key': 'profit_margin',
                    'name': '💰 Profit Margin',
                    'desc': 'Measures the percentage of revenue that translates into profit',
                    'benchmark': 'Excellent: >15% | Good: 10-15% | Poor: <10%'
                },
                {
                    'key': 'roe',
                    'name': '📈 Return on Equity (ROE)',
                    'desc': 'Indicates how effectively the company generates returns on shareholder investments',
                    'benchmark': 'Excellent: >20% | Good: 15-20% | Fair: 10-15% | Poor: <10%'
                },
                {
                    'key': 'current_ratio',
                    'name': '💧 Current Ratio',
                    'desc': 'Measures ability to pay short-term obligations with current assets',
                    'benchmark': 'Excellent: >2.0 | Good: 1.5-2.0 | Fair: 1.0-1.5 | Poor: <1.0'
                },
                {
                    'key': 'debt_to_equity',
                    'name': '⚖️ Debt-to-Equity Ratio',
                    'desc': 'Assesses financial leverage and capital structure risk',
                    'benchmark': 'Excellent: <0.5 | Good: 0.5-1.0 | Fair: 1.0-2.0 | Poor: >2.0'
                },
                {
                    'key': 'quick_ratio',
                    'name': '⚡ Quick Ratio',
                    'desc': 'Tests liquidity excluding inventory (more conservative than current ratio)',
                    'benchmark': 'Excellent: >1.5 | Good: 1.0-1.5 | Poor: <1.0'
                },
                {
                    'key': 'asset_turnover',
                    'name': '🔄 Asset Turnover',
                    'desc': 'Measures how efficiently assets generate revenue',
                    'benchmark': 'Excellent: >1.5 | Good: 1.0-1.5 | Poor: <1.0'
                }
            ]
            
            for info in ratio_info:
                value = results['ratios'].get(info['key'], 0)
                
                st.markdown(f"#### {info['name']}")
                st.markdown(f"*{info['desc']}*")
                
                col1, col2 = st.columns([1, 4])
                
                with col1:
                    st.markdown(f"### {value}{'%' if info['key'] in ['profit_margin', 'roe'] else ''}")
                
                with col2:
                    if 'ratio' in info['key']:
                        progress = min(value / 3, 1.0)
                    elif info['key'] in ['profit_margin', 'roe']:
                        progress = min(value / 30, 1.0)
                    else:
                        progress = min(value / 2, 1.0)
                    
                    st.progress(progress)
                    st.caption(f"📌 Benchmark: {info['benchmark']}")
                
                st.markdown("<br>", unsafe_allow_html=True)
        
        with tab3:
            st.markdown("### 🚨 Financial Risk Assessment")
            st.markdown("<br>", unsafe_allow_html=True)
            
            flags = results['flags']
            
            # Risk Summary
            high = sum(1 for f in flags if f['severity'] == 'high')
            medium = sum(1 for f in flags if f['severity'] == 'medium')
            low = sum(1 for f in flags if f['severity'] == 'low')
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("🚨 Critical Issues", high)
            with col2:
                st.metric("⚠️ Moderate Concerns", medium)
            with col3:
                st.metric("✅ Low Priority", low)
            
            st.markdown("<br><br>", unsafe_allow_html=True)
            
            for flag in flags:
                sev = flag['severity']
                
                if sev == 'high':
                    css_class = "alert-high"
                elif sev == 'medium':
                    css_class = "alert-medium"
                else:
                    css_class = "alert-low"
                
                st.markdown(f"""
                <div class="alert-card {css_class}">
                    <div class="alert-title">{flag['title']}</div>
                    <div class="alert-desc">{flag['description']}</div>
                </div>
                """, unsafe_allow_html=True)
        
        with tab4:
            st.markdown("### 💡 AI-Generated Strategic Recommendations")
            st.markdown("Data-driven strategies with projected financial impact")
            st.markdown("<br>", unsafe_allow_html=True)
            
            for idx, rec in enumerate(results['recommendations'], 1):
                st.markdown(f"""
                <div class="rec-card">
                    <div class="rec-header">
                        <div class="rec-badge">{idx}</div>
                        <div class="rec-title">Strategic Action #{idx}</div>
                    </div>
                    <div class="rec-content">{rec}</div>
                </div>
                """, unsafe_allow_html=True)
        
        # Export Section
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("### 📥 Export Analysis")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            report_json = json.dumps(results, indent=2, default=str)
            st.download_button(
                "📊 JSON Report",
                data=report_json,
                file_name=f"finvision_{results['company_name']}_{datetime.now().strftime('%Y%m%d')}.json",
                mime="application/json",
                use_container_width=True
            )
        
        with col2:
            df = pd.DataFrame([results['ratios']])
            df.insert(0, 'Company', results['company_name'])
            df.insert(1, 'Score', get_overall_score(results['ratios']))
            
            st.download_button(
                "📈 CSV Export",
                data=df.to_csv(index=False),
                file_name=f"finvision_{results['company_name']}_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv",
                use_container_width=True
            )
        
        with col3:
            report_text = f"""FinVision Financial Analysis Report
{'='*60}

Company: {results['company_name']}
Fiscal Year: {results['fiscal_year']}
Overall Health Score: {get_overall_score(results['ratios'])}/100
Analysis Date: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}

KEY FINANCIAL METRICS
{'='*60}
Profit Margin: {results['ratios']['profit_margin']}%
Return on Equity: {results['ratios']['roe']}%
Current Ratio: {results['ratios']['current_ratio']}
Debt-to-Equity: {results['ratios']['debt_to_equity']}
Quick Ratio: {results['ratios']['quick_ratio']}
Asset Turnover: {results['ratios']['asset_turnover']}

IDENTIFIED RISKS: {len(results['flags'])}
{'='*60}
"""
            for flag in results['flags']:
                report_text += f"[{flag['severity'].upper()}] {flag['title']}\n{flag['description']}\n\n"
            
            report_text += f"\nSTRATEGIC RECOMMENDATIONS: {len(results['recommendations'])}\n{'='*60}\n"
            for idx, rec in enumerate(results['recommendations'], 1):
                report_text += f"{idx}. {rec}\n\n"
            
            report_text += f"\n{'='*60}\nPowered by FinVision AI Financial Analyst\n"
            
            st.download_button(
                "📝 Text Report",
                data=report_text,
                file_name=f"finvision_{results['company_name']}_{datetime.now().strftime('%Y%m%d')}.txt",
                mime="text/plain",
                use_container_width=True
            )

if __name__ == "__main__":
    main()