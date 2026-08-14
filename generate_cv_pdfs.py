import os
import subprocess
import shutil
import pypdf

# Paths
OUTPUT_DIR = r"c:\Users\LENOVO\source\repos\sonnyariady.github.io"
ARTIFACT_DIR = r"C:\Users\LENOVO\.gemini\antigravity-ide\brain\84ce79b3-a508-400e-a99f-a889a2750ee1"
SCRATCH_DIR = os.path.join(OUTPUT_DIR, "scratch")
os.makedirs(SCRATCH_DIR, exist_ok=True)

DATE_SUFFIX = "23Aug2026"

# 1. Local CV HTML Template
html_local = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Sonny Ariady - Local CV</title>
<style>
  @page {
    size: A4;
    margin: 11mm 14mm 11mm 14mm;
  }
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }
  body {
    font-family: 'Segoe UI', Arial, Helvetica, sans-serif;
    font-size: 9.3pt;
    line-height: 1.37;
    color: #1a202c;
    background-color: #ffffff;
  }
  .header {
    margin-bottom: 10px;
  }
  .name {
    font-size: 21pt;
    font-weight: 800;
    color: #0f2b5c;
    letter-spacing: 0.5px;
    margin-bottom: 3px;
  }
  .title {
    font-size: 10.8pt;
    font-weight: 700;
    color: #1d4ed8;
    margin-bottom: 5px;
  }
  .contact-info {
    font-size: 8.8pt;
    color: #334155;
    margin-bottom: 6px;
  }
  .sep {
    color: #94a3b8;
    margin: 0 4px;
  }
  .divider-main {
    border-bottom: 2px solid #0f2b5c;
    margin-bottom: 8px;
  }
  
  .section-title {
    font-size: 10.2pt;
    font-weight: 800;
    color: #0f2b5c;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    border-bottom: 1px solid #cbd5e1;
    padding-bottom: 2px;
    margin-top: 9px;
    margin-bottom: 5px;
  }

  .summary p {
    text-align: justify;
    margin-bottom: 3px;
  }

  .skills-table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 3px;
  }
  .skills-table td {
    padding: 2px 0;
    vertical-align: top;
  }
  .skills-label {
    font-weight: 700;
    color: #0f2b5c;
    width: 25%;
    padding-right: 6px;
  }
  .skills-val {
    color: #1e293b;
    width: 75%;
  }

  .exp-item {
    margin-bottom: 7px;
    page-break-inside: avoid;
  }
  .exp-header {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 2px;
  }
  .exp-role-company {
    font-size: 9.5pt;
    color: #0f2b5c;
  }
  .exp-role {
    font-weight: 700;
  }
  .exp-company {
    font-weight: 700;
    color: #1e293b;
  }
  .exp-date {
    font-size: 8.8pt;
    font-weight: 700;
    color: #475569;
    white-space: nowrap;
  }
  
  ul.bullets {
    list-style-type: disc;
    margin-left: 15px;
    margin-top: 2px;
  }
  ul.bullets li {
    margin-bottom: 2px;
    text-align: justify;
  }

  .two-col {
    display: flex;
    gap: 16px;
  }
  .col-half {
    flex: 1;
  }

  .footer-note {
    margin-top: 8px;
    font-size: 8pt;
    color: #64748b;
    text-align: right;
  }
</style>
</head>
<body>

  <!-- HEADER -->
  <div class="header">
    <div class="name">SONNY ARIADY</div>
    <div class="title">Senior .NET Developer & AI-Assisted Software Engineer | Technical Consultant | Tech Lead</div>
    <div class="contact-info">
      Bekasi, West Java, Indonesia <span class="sep">|</span> +62 877-7665-7621 <span class="sep">|</span> sonnyariady@gmail.com <span class="sep">|</span> LinkedIn: linkedin.com/in/sonnyariady <span class="sep">|</span> GitHub: github.com/sonnyariady
    </div>
    <div class="divider-main"></div>
  </div>

  <!-- PROFESSIONAL SUMMARY -->
  <div class="section-title">Professional Summary</div>
  <div class="summary">
    <p>
      Senior .NET Engineer and Technical Consultant with <strong>15+ years of experience</strong> delivering high-performance enterprise applications across banking, FMCG, insurance, manufacturing, and telecommunications. <strong>Pioneer in AI-assisted software engineering</strong>, leveraging tools like GitHub Copilot, ChatGPT, Gemini, Perplexity, and Antigravity AI to accelerate development workflows, conduct deep error-log diagnostics, summarize and compare complex datasets, and streamline Linux/Ubuntu infrastructure deployment and troubleshooting. Hands-on expert in <strong>.NET 9, C#, ASP.NET APIs, Blazor, .NET MAUI Hybrid, microservices, and Docker/Nginx containerization</strong>. Proven track record in solution architecture, modernizing legacy systems, and technical leadership. Available for Full-Time, Hybrid, or Remote roles in Jabodetabek and Indonesia.
    </p>
  </div>

  <!-- TECHNICAL SKILLS & COMPETENCIES -->
  <div class="section-title">Technical Skills & Competencies</div>
  <table class="skills-table">
    <tr>
      <td class="skills-label">.NET & Architecture:</td>
      <td class="skills-val">.NET 9, C#, .NET Core, .NET Framework, ASP.NET MVC, ASP.NET Web API, Blazor, MudBlazor 7.4.0, .NET MAUI Hybrid, Microservices, Solution Architecture</td>
    </tr>
    <tr>
      <td class="skills-label">AI-Assisted Engineering:</td>
      <td class="skills-val">GitHub Copilot, ChatGPT, Gemini, Perplexity, Antigravity AI (Applied for AI-assisted coding, log diagnostics, data analysis & comparison, natural language ETL, and Linux/Ubuntu troubleshooting)</td>
    </tr>
    <tr>
      <td class="skills-label">Fullstack & Modern Web:</td>
      <td class="skills-val">React 19, TypeScript, Vite, Node.js & Express, Prisma ORM, PostgreSQL, TailwindCSS/Vanilla CSS</td>
    </tr>
    <tr>
      <td class="skills-label">DevOps & Infrastructure:</td>
      <td class="skills-val">Linux (Ubuntu), Nginx, Docker & Docker Compose, GitHub Actions CI/CD, Azure DevOps, Git, OpenTelemetry, SonarQube, JMeter</td>
    </tr>
    <tr>
      <td class="skills-label">Integration & Data:</td>
      <td class="skills-val">Apache Kafka, SAP Integration, Ultimus Workflow, Microsoft SQL Server, PostgreSQL, MongoDB, Redis, SSRS, Crystal Reports, REST & SOAP APIs</td>
    </tr>
    <tr>
      <td class="skills-label">Frontend & UI:</td>
      <td class="skills-val">Angular, AngularJS, JavaScript, jQuery, Bootstrap, Kendo UI, HTML5, CSS3</td>
    </tr>
  </table>

  <!-- PROFESSIONAL EXPERIENCE -->
  <div class="section-title">Professional Experience</div>

  <div class="exp-item">
    <div class="exp-header">
      <div class="exp-role-company">
        <span class="exp-role">Technical Consultant</span> <span class="sep">|</span> <span class="exp-company">PT Nexia Indonesia</span>
      </div>
      <div class="exp-date">Oct 2025 – Present</div>
    </div>
    <ul class="bullets">
      <li>Lead the migration of enterprise applications from OutSystems low-code to .NET 9 API architecture, significantly reducing platform licensing costs and improving maintainability.</li>
      <li>Utilize AI-assisted tools (Copilot, ChatGPT, Gemini, Antigravity AI) for rapid code synthesis, complex data comparison, error-log diagnostics, and Linux/Ubuntu deployment troubleshooting.</li>
      <li>Design reusable service patterns for CRUD operations, validation, advanced filtering, pagination, and automated Excel exports across core business modules.</li>
      <li>Deliver Blazor/MudBlazor 7.4.0 web applications and .NET MAUI Hybrid mobile solutions for cross-platform enterprise use cases.</li>
      <li>Implement CI/CD automation with GitHub Actions and Docker-based deployment workflows for Nginx/Linux environments.</li>
    </ul>
  </div>

  <div class="exp-item">
    <div class="exp-header">
      <div class="exp-role-company">
        <span class="exp-role">Senior .NET Developer</span> <span class="sep">|</span> <span class="exp-company">PT Kimberly-Clark Softex (via Tech Mahindra)</span>
      </div>
      <div class="exp-date">Jun 2025 – Sep 2025</div>
    </div>
    <ul class="bullets">
      <li>Stabilized legacy enterprise applications through targeted bug remediation, enhanced logging, and production issue resolution.</li>
      <li>Improved reporting efficiency and automated Excel export capabilities supporting critical business operations.</li>
      <li>Actively engaged in continuous technical upskilling via Tech Mahindra internal learning portal (exploring Node.js, React.js, Java Spring Boot) to maintain enterprise readiness for multi-stack deployment.</li>
    </ul>
  </div>

  <div class="exp-item">
    <div class="exp-header">
      <div class="exp-role-company">
        <span class="exp-role">.NET Developer</span> <span class="sep">|</span> <span class="exp-company">PT AIA Indonesia (via Glints)</span>
      </div>
      <div class="exp-date">Aug 2024 – May 2025</div>
    </div>
    <ul class="bullets">
      <li>Developed core REST APIs and Blazor applications supporting agent (ABDPlus) and customer management platforms.</li>
      <li>Enhanced observability through OpenTelemetry implementation and successfully delivered security remediation for penetration-testing findings (Veracode).</li>
    </ul>
  </div>

  <div class="exp-item">
    <div class="exp-header">
      <div class="exp-role-company">
        <span class="exp-role">Senior .NET Backend Developer</span> <span class="sep">|</span> <span class="exp-company">PT Bukit Makmur Mandiri Utama</span>
      </div>
      <div class="exp-date">Aug 2022 – Aug 2024</div>
    </div>
    <ul class="bullets">
      <li>Designed backend architecture for modular enterprise applications (including MIGO Online SAP Integration & CRF Online Workflow) and supported modernization initiatives improving scalability.</li>
      <li>Strengthened code quality and security compliance through SonarQube governance and standardized engineering practices.</li>
    </ul>
  </div>

  <div class="exp-item">
    <div class="exp-header">
      <div class="exp-role-company">
        <span class="exp-role">Senior .NET Backend Developer</span> <span class="sep">|</span> <span class="exp-company">PT Alpha Indosoft</span>
      </div>
      <div class="exp-date">Apr 2021 – Aug 2022</div>
    </div>
    <ul class="bullets">
      <li>Refactored monolithic enterprise APIs into scalable microservice architectures and created automated reporting schedulers.</li>
      <li>Implemented Kafka-based event integration and Telegram monitoring solutions to accelerate incident response times.</li>
    </ul>
  </div>

  <div class="exp-item">
    <div class="exp-header">
      <div class="exp-role-company">
        <span class="exp-role">.NET Developer Roles</span> <span class="sep">|</span> <span class="exp-company">Job Tomori, Berlian Sistem Informasi, Accenture, Bank Negara Indonesia (BNI)</span>
      </div>
      <div class="exp-date">2014 – 2021</div>
    </div>
    <ul class="bullets">
      <li><strong>BNI (2014–2017):</strong> Led technical migration of legacy PHP internal applications to modern .NET and SQL Server architecture; developed eOffice and banking APIs.</li>
      <li><strong>Accenture & BSI (2017–2020):</strong> Delivered fleet management, pricing platforms, modern workflow integrations, and APIs using Agile, Azure DevOps, and Git.</li>
      <li><strong>Job Tomori (2020–2021):</strong> Developed end-to-end .NET and Angular applications with SOAP integrations and workflow automation.</li>
    </ul>
  </div>

  <!-- FEATURED CASE STUDIES & PROJECTS (LATEST UPDATES) -->
  <div class="section-title">Featured Portfolio & Case Studies</div>
  <ul class="bullets">
    <li><strong>Tukang Sayur Online (Web & Mobile):</strong> Real-time hyper-local vegetable commerce platform built with .NET 9, Blazor Server & MAUI Hybrid, MudBlazor 7.4.0, ASP.NET Core API, and PostgreSQL (GitHub: github.com/sonnyariady/TukangSayurOnline).</li>
    <li><strong>TukangRoti (Sonny Bakery POS):</strong> Fullstack bakery production, inventory, POS cashier, and order management system built with React 19, TypeScript, Vite, Node.js & Express, Prisma ORM, and PostgreSQL (GitHub: github.com/sonnyariady/TukangRoti).</li>
    <li><strong>Monthly Expense Tracker & AI Data Pipeline:</strong> Fullstack expense management (React 18, FastAPI, SQLite, GitHub: github.com/sonnyariady/vibe-expense-tracker) and automated C# .NET 9 + Antigravity AI ETL pipeline for SQL Server to PostgreSQL data migration.</li>
  </ul>

  <!-- EARLIER EXPERIENCE -->
  <div class="section-title">Earlier Experience</div>
  <ul class="bullets">
    <li><strong>Tower Bersama Group (2017):</strong> .NET Developer – Enhanced HR employee management systems using VB.NET and ASP.NET Web Forms.</li>
    <li><strong>Integrasi Solution (2009–2014):</strong> .NET Developer – Delivered enterprise workflow solutions using Ultimus Workflow & Web Form Generator.</li>
    <li><strong>Global Administrasi Solusi (2006–2007):</strong> Junior Developer – Developed Crystal Reports and automated recurring reporting processes.</li>
  </ul>

  <!-- EDUCATION & CERTIFICATIONS -->
  <div class="two-col" style="margin-top: 3px;">
    <div class="col-half">
      <div class="section-title">Education</div>
      <ul class="bullets" style="margin-left: 12px;">
        <li><strong>Master of Engineering in Informatics (M.T.)</strong><br>Institut Teknologi Bandung (ITB) (2007–2009)</li>
        <li style="margin-top: 2px;"><strong>Bachelor of Engineering in Informatics (S.T.)</strong><br>Universitas Trisakti (2001–2006)</li>
      </ul>
    </div>
    <div class="col-half">
      <div class="section-title">Certifications</div>
      <ul class="bullets" style="margin-left: 12px;">
        <li><strong>MCPD:</strong> Windows Developer 3.5 (2010)</li>
        <li><strong>MCTS:</strong> .NET Framework 3.5 (2009)</li>
        <li><strong>MCP:</strong> Microsoft Certified Professional (2009)</li>
      </ul>
    </div>
  </div>

  <div class="footer-note">Updated: August 23, 2026</div>

</body>
</html>
"""

# 2. International CV HTML Template
html_international = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Sonny Ariady - International CV</title>
<style>
  @page {
    size: A4;
    margin: 11mm 14mm 11mm 14mm;
  }
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }
  body {
    font-family: 'Segoe UI', Arial, Helvetica, sans-serif;
    font-size: 9.1pt;
    line-height: 1.35;
    color: #1e293b;
    background-color: #ffffff;
  }
  .header {
    text-align: center;
    margin-bottom: 10px;
  }
  .name {
    font-size: 21pt;
    font-weight: 800;
    color: #0f2b5c;
    letter-spacing: 0.8px;
    margin-bottom: 3px;
    text-transform: uppercase;
  }
  .title {
    font-size: 10.5pt;
    font-weight: 700;
    color: #1d4ed8;
    margin-bottom: 5px;
  }
  .contact-info {
    font-size: 8.8pt;
    color: #475569;
    margin-bottom: 3px;
  }
  .sep {
    color: #94a3b8;
    margin: 0 4px;
  }

  .section-title {
    font-size: 9.8pt;
    font-weight: 800;
    color: #0f2b5c;
    text-transform: uppercase;
    letter-spacing: 0.6px;
    border-bottom: 1px solid #cbd5e1;
    padding-bottom: 2px;
    margin-top: 9px;
    margin-bottom: 4px;
  }

  p {
    text-align: justify;
    margin-bottom: 3px;
  }

  .relocation-box {
    background-color: #f8fafc;
    border-left: 3px solid #1d4ed8;
    padding: 5px 9px;
    margin-bottom: 4px;
    font-size: 8.8pt;
  }

  .competencies-text {
    font-size: 8.7pt;
    color: #1e293b;
    line-height: 1.38;
    margin-bottom: 3px;
  }

  .skills-table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 3px;
  }
  .skills-table td {
    padding: 1.8px 0;
    vertical-align: top;
  }
  .skills-label {
    font-weight: 700;
    color: #0f2b5c;
    width: 24%;
    padding-right: 6px;
  }
  .skills-val {
    color: #334155;
    width: 76%;
  }

  .exp-item {
    margin-bottom: 6px;
    page-break-inside: avoid;
  }
  .exp-header {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 2px;
  }
  .exp-company-role {
    font-size: 9.3pt;
  }
  .exp-company {
    font-weight: 700;
    color: #0f2b5c;
  }
  .exp-role {
    font-weight: 700;
    color: #1d4ed8;
  }
  .exp-date {
    font-size: 8.6pt;
    font-weight: 700;
    color: #475569;
    white-space: nowrap;
  }
  
  ul.bullets {
    list-style-type: disc;
    margin-left: 15px;
    margin-top: 2px;
  }
  ul.bullets li {
    margin-bottom: 2px;
    text-align: justify;
  }

  .footer {
    display: flex;
    justify-content: space-between;
    margin-top: 10px;
    font-size: 8pt;
    color: #64748b;
    border-top: 1px solid #e2e8f0;
    padding-top: 4px;
  }
</style>
</head>
<body>

  <!-- HEADER -->
  <div class="header">
    <div class="name">SONNY ARIADY</div>
    <div class="title">Technical Consultant | Senior .NET Engineer | Enterprise Application Modernization</div>
    <div class="contact-info">
      Bekasi, West Java, Indonesia <span class="sep">|</span> +62 877-7665-7621 <span class="sep">|</span> sonnyariady@gmail.com
    </div>
    <div class="contact-info">
      LinkedIn: linkedin.com/in/sonnyariady <span class="sep">|</span> GitHub: github.com/sonnyariady
    </div>
  </div>

  <!-- PROFESSIONAL SUMMARY -->
  <div class="section-title">Professional Summary</div>
  <p>
    Technical Consultant and Senior .NET Engineer with <strong>15+ years of experience</strong> delivering enterprise applications across banking, insurance, FMCG, manufacturing, telecommunications, and technology sectors. Expertise in <strong>.NET 9, C#, ASP.NET APIs, Blazor, .NET MAUI Hybrid, application modernization, workflow automation, systems integration, and SQL-based platforms</strong>. Combines hands-on engineering with solution design, stakeholder engagement, production support, security remediation, and modernization of legacy low-code/monolithic systems. Experienced in AI-assisted development tools (ChatGPT, Copilot, Gemini, Perplexity, Antigravity AI) for rapid solution synthesis.
  </p>

  <!-- RELOCATION & WORK AUTHORIZATION -->
  <div class="section-title">Relocation & Work Authorization</div>
  <div class="relocation-box">
    Based in Bekasi, West Java, Indonesia. <strong>Open to relocation</strong> for suitable roles across Europe, Singapore, Malaysia, Australia, and New Zealand. Employer-sponsored visa/work permit or relocation support required. Available to relocate on an agreed timeline and familiar with cross-border employment arrangements through Employer of Record (EOR) providers such as Deel and Remote.
  </div>

  <!-- CORE COMPETENCIES -->
  <div class="section-title">Core Competencies</div>
  <div class="competencies-text">
    <strong>Enterprise Application Modernization</strong> &bull; Solution Design &bull; Backend Architecture &bull; REST & SOAP APIs &bull; Microservices &bull; Cross-Platform Web & Mobile Development &bull; Workflow Automation &bull; Systems Integration &bull; Production Support &bull; Security Remediation & Pentest Governance &bull; Stakeholder Management &bull; Business Analysis
  </div>

  <!-- TECHNICAL SKILLS -->
  <div class="section-title">Technical Skills</div>
  <table class="skills-table">
    <tr>
      <td class="skills-label">.NET & Architecture:</td>
      <td class="skills-val">.NET 9, C#, .NET Core, .NET Framework, ASP.NET MVC, ASP.NET Web API, Blazor, MudBlazor 7.4.0, .NET MAUI Hybrid, Microservices, REST APIs, SOAP services</td>
    </tr>
    <tr>
      <td class="skills-label">Modern Web & Fullstack:</td>
      <td class="skills-val">React 19, TypeScript, Vite, Node.js & Express, Prisma ORM, PostgreSQL, TailwindCSS/Vanilla CSS</td>
    </tr>
    <tr>
      <td class="skills-label">Integration & Workflow:</td>
      <td class="skills-val">Apache Kafka, SAP Integration, Ultimus Workflow, business process automation, custom workflow development, API integration</td>
    </tr>
    <tr>
      <td class="skills-label">Frontend UI:</td>
      <td class="skills-val">Angular, AngularJS, JavaScript, jQuery, Bootstrap, Kendo UI, HTML5, CSS3</td>
    </tr>
    <tr>
      <td class="skills-label">Data & Reporting:</td>
      <td class="skills-val">Microsoft SQL Server, PostgreSQL, MongoDB, Redis, SSRS, Crystal Reports, wkhtmltopdf, Excel reporting & automated export</td>
    </tr>
    <tr>
      <td class="skills-label">DevOps & Observability:</td>
      <td class="skills-val">GitHub Actions CI/CD, Azure DevOps, Git, Docker & Docker Compose, Linux (Ubuntu), Nginx, OpenTelemetry, SonarQube, JMeter, Redgate SQL Toolbelt, Visual Studio, VS Code</td>
    </tr>
    <tr>
      <td class="skills-label">AI-Assisted Development:</td>
      <td class="skills-val">ChatGPT, GitHub Copilot, Gemini, Perplexity, Antigravity AI (Prompt engineering, code synthesis, log diagnostics, ETL automation)</td>
    </tr>
  </table>

  <!-- PROFESSIONAL EXPERIENCE -->
  <div class="section-title">Professional Experience</div>

  <div class="exp-item">
    <div class="exp-header">
      <div class="exp-company-role">
        <span class="exp-company">PT Nexia Indonesia</span> - <span class="exp-role">Technical Consultant</span>
      </div>
      <div class="exp-date">Oct 2025 - Present</div>
    </div>
    <ul class="bullets">
      <li>Lead migration of enterprise applications from OutSystems low-code to .NET 9 API architecture, reducing platform dependency and licensing costs while improving maintainability.</li>
      <li>Design reusable service patterns for CRUD operations, validation, advanced filtering, pagination, and Excel export across business modules.</li>
      <li>Deliver Blazor and MudBlazor web applications together with .NET MAUI Hybrid mobile solutions for cross-platform use cases.</li>
      <li>Implement CI/CD automation with GitHub Actions and Docker-based deployment workflows for Linux environments.</li>
      <li>Partner with stakeholders and end-users to translate complex business processes into scalable, supportable technical solutions.</li>
    </ul>
  </div>

  <div class="exp-item">
    <div class="exp-header">
      <div class="exp-company-role">
        <span class="exp-company">PT Kimberly-Clark Softex (via Tech Mahindra)</span> - <span class="exp-role">.NET Developer</span>
      </div>
      <div class="exp-date">Jun 2025 - Sep 2025</div>
    </div>
    <ul class="bullets">
      <li>Stabilized legacy enterprise applications through targeted bug remediation, enhanced logging, and production issue resolution.</li>
      <li>Improved reporting and Excel export capabilities supporting critical business operations.</li>
      <li>Completed technical upskilling modules on Tech Mahindra's internal learning portal across multi-stack frameworks (Node.js, React.js, Spring Boot) for project deployment readiness.</li>
    </ul>
  </div>

  <div class="exp-item">
    <div class="exp-header">
      <div class="exp-company-role">
        <span class="exp-company">PT AIA Indonesia (via Glints)</span> - <span class="exp-role">.NET Developer</span>
      </div>
      <div class="exp-date">Aug 2024 - May 2025</div>
    </div>
    <ul class="bullets">
      <li>Developed APIs and Blazor applications supporting agent (ABDPlus) and customer management platforms.</li>
      <li>Enhanced observability through telemetry and monitoring implementation, and delivered security remediation for penetration-testing findings (Veracode).</li>
    </ul>
  </div>

  <div class="exp-item">
    <div class="exp-header">
      <div class="exp-company-role">
        <span class="exp-company">PT Bukit Makmur Mandiri Utama</span> - <span class="exp-role">Senior .NET Backend Developer</span>
      </div>
      <div class="exp-date">Aug 2022 - Aug 2024</div>
    </div>
    <ul class="bullets">
      <li>Designed backend architecture for modular enterprise applications (including MIGO Online SAP Integration & CRF Online Workflow) and supported modernization initiatives improving scalability and maintainability.</li>
      <li>Strengthened code quality and security compliance through SonarQube governance and engineering standards.</li>
    </ul>
  </div>

  <div class="exp-item">
    <div class="exp-header">
      <div class="exp-company-role">
        <span class="exp-company">PT Alpha Indosoft</span> - <span class="exp-role">Senior .NET Backend Developer</span>
      </div>
      <div class="exp-date">Apr 2021 - Aug 2022</div>
    </div>
    <ul class="bullets">
      <li>Refactored enterprise APIs into scalable architectures and developed automated reporting schedulers.</li>
      <li>Implemented Kafka-based integrations and Telegram monitoring solutions to accelerate incident response.</li>
    </ul>
  </div>

  <div class="exp-item">
    <div class="exp-header">
      <div class="exp-company-role">
        <span class="exp-company">PT Job Tomori</span> - <span class="exp-role">.NET Developer</span>
      </div>
      <div class="exp-date">Apr 2020 - Mar 2021</div>
    </div>
    <ul class="bullets">
      <li>Developed end-to-end applications using .NET and Angular, including SOAP integration and workflow automation.</li>
    </ul>
  </div>

  <div class="exp-item">
    <div class="exp-header">
      <div class="exp-company-role">
        <span class="exp-company">PT Berlian Sistem Informasi</span> - <span class="exp-role">.NET Developer</span>
      </div>
      <div class="exp-date">Jan 2018 - Mar 2020</div>
    </div>
    <ul class="bullets">
      <li>Modernized legacy applications and integration services, and developed APIs supporting mobile and workflow initiatives.</li>
    </ul>
  </div>

  <div class="exp-item">
    <div class="exp-header">
      <div class="exp-company-role">
        <span class="exp-company">Accenture Indonesia</span> - <span class="exp-role">.NET Developer</span>
      </div>
      <div class="exp-date">Aug 2017 - Dec 2017</div>
    </div>
    <ul class="bullets">
      <li>Contributed to fleet management and pricing platform initiatives using Agile delivery practices, Azure DevOps, and Git.</li>
    </ul>
  </div>

  <div class="exp-item">
    <div class="exp-header">
      <div class="exp-company-role">
        <span class="exp-company">Bank Negara Indonesia</span> - <span class="exp-role">.NET Developer</span>
      </div>
      <div class="exp-date">2014 - 2017</div>
    </div>
    <ul class="bullets">
      <li>Led migration of legacy PHP applications to .NET and SQL Server architecture.</li>
      <li>Developed eOffice and operational banking applications, including APIs supporting Android integration.</li>
    </ul>
  </div>

  <!-- FEATURED PROJECTS & CASE STUDIES -->
  <div class="section-title">Featured Projects & Case Studies</div>
  <ul class="bullets">
    <li><strong>Tukang Sayur Online (Web & Mobile):</strong> Cross-platform hyper-local e-commerce platform built with .NET 9, Blazor Server & MAUI Hybrid, MudBlazor 7.4.0, ASP.NET Core API, and PostgreSQL (GitHub: github.com/sonnyariady/TukangSayurOnline).</li>
    <li><strong>TukangRoti (Sonny Bakery POS):</strong> Fullstack bakery POS cashier, inventory, and order management system built with React 19, TypeScript, Vite, Node.js & Express, Prisma ORM, and PostgreSQL (GitHub: github.com/sonnyariady/TukangRoti).</li>
    <li><strong>Monthly Expense Tracker:</strong> Fullstack household expense management built with React 18, FastAPI, SQLite, and AI-assisted development (GitHub: github.com/sonnyariady/vibe-expense-tracker).</li>
  </ul>

  <!-- EARLIER EXPERIENCE -->
  <div class="section-title">Earlier Experience</div>
  <ul class="bullets">
    <li><strong>Tower Bersama Group - .NET Developer | 2017:</strong> Delivered enhancements for employee management applications using VB.NET and ASP.NET Web Forms.</li>
    <li><strong>Integrasi Solution - .NET Developer | 2009 - 2014:</strong> Delivered enterprise workflow solutions using Ultimus Workflow and created a reusable Web Form Generator framework.</li>
    <li><strong>Global Administrasi Solusi - Junior Developer | 2006 - 2007:</strong> Developed Crystal Reports and automated recurring reporting activities.</li>
  </ul>

  <!-- EDUCATION -->
  <div class="section-title">Education</div>
  <ul class="bullets">
    <li><strong>Institut Teknologi Bandung (ITB)</strong> - Master of Engineering in Informatics | 2007 - 2009</li>
    <li><strong>Universitas Trisakti</strong> - Bachelor of Engineering in Informatics | 2001 - 2006</li>
  </ul>

  <!-- CERTIFICATIONS -->
  <div class="section-title">Certifications</div>
  <ul class="bullets">
    <li>Microsoft Certified Professional (MCP) - 2009</li>
    <li>Microsoft Certified Technology Specialist (MCTS): .NET Framework 3.5 Windows Forms Application Development - 2009</li>
    <li>Microsoft Certified Professional Developer (MCPD): Windows Developer 3.5 - 2010</li>
  </ul>

  <div class="footer">
    <span>Sonny Ariady | CV</span>
    <span>Updated: August 23, 2026</span>
  </div>

</body>
</html>
"""

html_local_path = os.path.join(SCRATCH_DIR, "cv_local.html")
html_int_path = os.path.join(SCRATCH_DIR, "cv_international.html")

pdf_local_name = f"Sonny_Ariady_CV_Local_{DATE_SUFFIX}.pdf"
pdf_int_name = f"Sonny_Ariady_CV_International_{DATE_SUFFIX}.pdf"

pdf_local_path = os.path.join(OUTPUT_DIR, pdf_local_name)
pdf_int_path = os.path.join(OUTPUT_DIR, pdf_int_name)

pdf_local_art = os.path.join(ARTIFACT_DIR, pdf_local_name)
pdf_int_art = os.path.join(ARTIFACT_DIR, pdf_int_name)

with open(html_local_path, "w", encoding="utf-8") as f:
    f.write(html_local)

with open(html_int_path, "w", encoding="utf-8") as f:
    f.write(html_international)

print("HTML files updated.")

edge_cmd = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

# Convert Local CV
res1 = subprocess.run([
    edge_cmd,
    "--headless",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_local_path}",
    html_local_path
], capture_output=True, text=True)

# Convert International CV
res2 = subprocess.run([
    edge_cmd,
    "--headless",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_int_path}",
    html_int_path
], capture_output=True, text=True)

print("Local PDF returncode:", res1.returncode)
print("International PDF returncode:", res2.returncode)

# Copy to artifacts directory
shutil.copyfile(pdf_local_path, pdf_local_art)
shutil.copyfile(pdf_int_path, pdf_int_art)
print("Copied PDFs to artifact directory.")

# Page count check
r1 = pypdf.PdfReader(pdf_local_path)
r2 = pypdf.PdfReader(pdf_int_path)
print(f"Local PDF ({pdf_local_name}) Pages: {len(r1.pages)}")
print(f"International PDF ({pdf_int_name}) Pages: {len(r2.pages)}")
