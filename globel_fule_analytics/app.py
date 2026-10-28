"""
Global Fuel Prices and Taxation Trends: A Comprehensive Analysis
Flask Web Application for Tableau Analytics Showcase
"""

import os
from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
# Secret key for flash messages and session handling
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'global-fuel-analytics-secure-key-2026')

# ==============================================================================
# TABLEAU PUBLIC CONFIGURATION
# ------------------------------------------------------------------------------
# STEP FOR BEGINNERS:
# Replace the URLs below with your own published Tableau Public Dashboard & Story URLs.
# Example format:
# "https://public.tableau.com/views/YourWorkbookName/YourDashboardName"
# "https://public.tableau.com/views/YourWorkbookName/YourStoryName"
# ==============================================================================
DEFAULT_TABLEAU_DASHBOARD_URL = os.environ.get(
    'TABLEAU_DASHBOARD_URL',
    'https://public.tableau.com/views/Globelfulepriseandtaxationtrends/GlobalFuelPriceDashboard?:language=en-GB&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link'
)

DEFAULT_TABLEAU_STORY_URL = os.environ.get(
    'TABLEAU_STORY_URL',
    'https://public.tableau.com/views/Globelfulepriseandtaxationtrends/GlobalFuelPriceDashboard?:language=en-GB&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link'
)


def check_is_placeholder(url: str) -> bool:
    """Helper to detect if the URL is still a placeholder or demo workbook."""
    placeholders = ['RegionalSampleWorkbook', 'your-username', 'placeholder', 'example']
    return any(p.lower() in url.lower() for p in placeholders)


def clean_tableau_embed_url(url: str) -> str:
    """Helper to generate a clean, responsive embed URL for Tableau Public."""
    if not url:
        return ""
    # Strip any existing query params from share links (e.g., ?:language=...&:origin=...)
    base_url = url.split('?')[0].strip()
    return f"{base_url}?:showVizHome=no&:embed=true&:toolbar=yes"


@app.context_processor
def inject_global_data():
    """Make project metadata available across all Jinja2 templates."""
    active_tableau_url = 'https://public.tableau.com/views/Globelfulepriseandtaxationtrends/GlobalFuelPriceDashboard?:language=en-GB&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link'
    return {
        'project_title': 'Global Fuel Prices and Taxation Trends',
        'project_subtitle': 'A Comprehensive Analysis of Retail Energy Economics & Fiscal Policies',
        'app_name': 'Global Fuel Analytics',
        'author_name': 'Student Data Analyst',
        'tableau_public_url': active_tableau_url,
        'tableau_embed_url': clean_tableau_embed_url(active_tableau_url),
        'version': '1.0.0'
    }


@app.route('/')
def home():
    """Home / Landing page route with hero section, summary cards, and project objectives."""
    return render_template('index.html', active_page='home')


@app.route('/dashboard')
def dashboard():
    """Interactive Tableau Dashboard page route with responsive embed container."""
    is_placeholder = check_is_placeholder(DEFAULT_TABLEAU_DASHBOARD_URL)
    dashboard_embed_url = clean_tableau_embed_url(DEFAULT_TABLEAU_DASHBOARD_URL)
    return render_template(
        'dashboard.html',
        active_page='dashboard',
        dashboard_url=DEFAULT_TABLEAU_DASHBOARD_URL,
        dashboard_embed_url=dashboard_embed_url,
        is_placeholder=is_placeholder
    )


@app.route('/story')
def story():
    """Tableau Story page route presenting step-by-step narrative and findings."""
    is_placeholder = check_is_placeholder(DEFAULT_TABLEAU_STORY_URL)
    story_embed_url = clean_tableau_embed_url(DEFAULT_TABLEAU_STORY_URL)
    return render_template(
        'story.html',
        active_page='story',
        story_url=DEFAULT_TABLEAU_STORY_URL,
        story_embed_url=story_embed_url,
        is_placeholder=is_placeholder
    )


@app.route('/about')
def about():
    """Project methodology, data dictionary, tools, and analytical boundaries."""
    dataset_fields = [
        {"name": "Country", "type": "Categorical (String)", "desc": "Sovereign nation or territory name."},
        {"name": "Date", "type": "Temporal (Date)", "desc": "Observation period / timestamp of recorded fuel price and benchmark rates."},
        {"name": "Income Level", "type": "Categorical (Ordinal)", "desc": "World Bank classification (High, Upper-Middle, Lower-Middle, Low income)."},
        {"name": "Region", "type": "Categorical (Geographical)", "desc": "Geographic continent or regional economic bloc."},
        {"name": "Subsidy Level", "type": "Categorical / Ordinal", "desc": "Government fuel subsidy intensity tier (High, Medium, Low, None)."},
        {"name": "Brent Crude USD", "type": "Numerical (Continuous)", "desc": "Global benchmark international crude oil spot price in USD per barrel."},
        {"name": "Diesel USD Liter", "type": "Numerical (Continuous)", "desc": "Domestic pump price of diesel fuel converted to USD per liter."},
        {"name": "LPG USD Liter", "type": "Numerical (Continuous)", "desc": "Domestic retail liquefied petroleum gas price in USD per liter equivalent."},
        {"name": "Petrol USD Liter", "type": "Numerical (Continuous)", "desc": "Domestic pump price of gasoline/petrol converted to USD per liter."},
        {"name": "Tax Percentage", "type": "Numerical (Percentage)", "desc": "Combined fiscal excise duty and sales tax / VAT as a percentage of retail price."}
    ]
    return render_template('about.html', active_page='about', dataset_fields=dataset_fields)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact & feedback route with client message confirmation."""
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        subject = request.form.get('subject', '').strip()
        message = request.form.get('message', '').strip()

        if not name or not email or not message:
            flash("Please complete all required fields (Name, Email, and Message).", "danger")
        else:
            flash(f"Thank you, {name}! Your message regarding '{subject or 'Fuel Analytics Project'}' has been received successfully.", "success")
            return redirect(url_for('contact'))

    return render_template('contact.html', active_page='contact')


@app.errorhandler(404)
def page_not_found(e):
    """Custom 404 error handler with friendly recovery links."""
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    """Custom 500 error handler."""
    return render_template('404.html', error_code=500, error_message="Internal Server Error"), 500


if __name__ == '__main__':
    # Run development server on local interface
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port, debug=True)

