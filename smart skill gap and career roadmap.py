
import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import random
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

CAREERS = {
    "Data Scientist": {
        "skills": "python statistics sql numpy pandas machine learning data visualization",
        "interests": "data maths research ai problem solving",
        "desc": "Uses statistics and data to discover patterns and make predictions.",
        "roadmap": [
            ("Weeks 1-3: Python", "Variables, loops, functions, lists and dictionaries.", "Practice Python problems."),
            ("Weeks 4-6: Data Tools", "NumPy, Pandas, filtering and data cleaning.", "Analyze student marks."),
            ("Weeks 7-9: Statistics", "Probability, averages, correlation and graphs.", "Create a data dashboard."),
            ("Weeks 10-13: ML and SQL", "SQL queries, regression and classification.", "Build a prediction model."),
            ("Weeks 14-17: Projects", "Data cleaning, analysis and model evaluation.", "Complete two projects."),
            ("Weeks 18-20: Jobs", "Resume, GitHub, interviews and applications.", "Prepare your portfolio.")
        ],
        "projects": "Sales Analysis, Student Performance, House Price Prediction",
        "interview": "Python, SQL joins, statistics, missing values, overfitting, model evaluation"
    },
    "Data Analyst": {
        "skills": "excel sql python statistics data visualization power bi pandas",
        "interests": "data business reporting maths research problem solving",
        "desc": "Analyzes data and creates reports and dashboards.",
        "roadmap": [
            ("Weeks 1-3: Excel", "Formulas, filters, lookups and pivot tables.", "Create a marks report."),
            ("Weeks 4-6: SQL", "Queries, joins, grouping and sorting.", "Solve SQL exercises."),
            ("Weeks 7-9: Python", "Pandas, cleaning and grouping data.", "Analyze sales data."),
            ("Weeks 10-12: Dashboards", "Charts, Power BI and data storytelling.", "Create a dashboard."),
            ("Weeks 13-15: Projects", "Combine SQL, analysis and charts.", "Complete two projects."),
            ("Weeks 16-18: Jobs", "Resume, interview practice and applications.", "Build a portfolio.")
        ],
        "projects": "Sales Dashboard, College Attendance, E-commerce Analysis",
        "interview": "Excel, SQL joins, KPIs, data cleaning, charts, business insights"
    },
    "AI/ML Engineer": {
        "skills": "python statistics numpy pandas machine learning deep learning sql",
        "interests": "ai automation maths research technology problem solving",
        "desc": "Develops and evaluates machine learning and AI applications.",
        "roadmap": [
            ("Weeks 1-4: Python", "Programming, functions, OOP and debugging.", "Build a Python app."),
            ("Weeks 5-7: Mathematics", "Statistics, linear algebra, NumPy and Pandas.", "Explore a dataset."),
            ("Weeks 8-12: ML", "Regression, classification and model evaluation.", "Train a simple model."),
            ("Weeks 13-17: Deep Learning", "Neural networks, activation and loss.", "Build a learning demo."),
            ("Weeks 18-22: Projects", "Data preparation and model testing.", "Build an AI project."),
            ("Weeks 23-26: Jobs", "Revise ML, Python and interview topics.", "Publish your portfolio.")
        ],
        "projects": "Spam Detection, Movie Recommendation, Churn Prediction",
        "interview": "Supervised learning, regression, overfitting, precision, recall, neural networks"
    },
    "Python Developer": {
        "skills": "python oop sql git debugging apis problem solving",
        "interests": "coding automation technology problem solving",
        "desc": "Builds applications, scripts and software using Python.",
        "roadmap": [
            ("Weeks 1-4: Python", "Data types, loops, functions and collections.", "Solve coding problems."),
            ("Weeks 5-7: OOP", "Classes, objects, modules and exceptions.", "Build a management system."),
            ("Weeks 8-10: SQL", "Queries, file handling and debugging.", "Add data handling."),
            ("Weeks 11-13: APIs and Git", "API basics, GitHub and testing.", "Build a small application."),
            ("Weeks 14-17: Projects", "Modular code and documentation.", "Complete two applications."),
            ("Weeks 18-20: Jobs", "DSA, Python revision and interviews.", "Prepare a portfolio.")
        ],
        "projects": "Expense Tracker, Library System, Student Information System",
        "interview": "Python collections, OOP, exceptions, SQL, debugging, DSA"
    },
    "Web Developer": {
        "skills": "html css javascript git web development sql python",
        "interests": "websites design coding creativity technology",
        "desc": "Creates interactive websites and web applications.",
        "roadmap": [
            ("Weeks 1-3: HTML", "Forms, links, tables and page structure.", "Build a webpage."),
            ("Weeks 4-6: CSS", "Layouts, colors and responsive design.", "Improve webpage design."),
            ("Weeks 7-10: JavaScript", "Functions, events and DOM.", "Add interactive features."),
            ("Weeks 11-12: Git", "Repositories, commits and README files.", "Upload your code."),
            ("Weeks 13-16: Projects", "Combine HTML, CSS and JavaScript.", "Build two websites."),
            ("Weeks 17-20: Jobs", "Portfolio and interview preparation.", "Apply for internships.")
        ],
        "projects": "Portfolio, Food Ordering Website, College Website",
        "interview": "HTML forms, CSS box model, JavaScript, DOM, GitHub"
    },
    "Cybersecurity Analyst": {
        "skills": "networking linux python security operating systems problem solving",
        "interests": "security investigation networks technology problem solving",
        "desc": "Helps detect security risks and protect computer systems.",
        "roadmap": [
            ("Weeks 1-4: Fundamentals", "Operating systems and networking.", "Study network basics."),
            ("Weeks 5-8: Linux", "Commands, permissions and processes.", "Practice Linux."),
            ("Weeks 9-12: Security", "Authentication, threats and safe practices.", "Create a security checklist."),
            ("Weeks 13-16: Logs", "Read logs and identify unusual patterns.", "Build a log analyzer."),
            ("Weeks 17-20: Labs", "Practice in authorized training labs.", "Document lab exercises."),
            ("Weeks 21-22: Jobs", "Revise networks and security concepts.", "Prepare interviews.")
        ],
        "projects": "Log Analyzer, Password Strength Checker, Network Monitoring",
        "interview": "TCP/IP, DNS, Linux, authentication, logs, security ethics"
    },
    "UI/UX Designer": {
        "skills": "figma design prototyping wireframing user research communication",
        "interests": "design creativity websites user experience psychology",
        "desc": "Designs useful and accessible digital experiences.",
        "roadmap": [
            ("Weeks 1-3: Design", "Color, typography, spacing and accessibility.", "Redesign a webpage."),
            ("Weeks 4-6: Wireframes", "User flows and screen layouts.", "Design an app flow."),
            ("Weeks 7-9: Figma", "Components and interactive prototypes.", "Create a prototype."),
            ("Weeks 10-12: Research", "User feedback and usability testing.", "Test your design."),
            ("Weeks 13-16: Projects", "Document design decisions and improvements.", "Create two case studies."),
            ("Weeks 17-18: Jobs", "Portfolio and design interviews.", "Prepare your portfolio.")
        ],
        "projects": "Food App Prototype, College App Design, Shopping App",
        "interview": "UI vs UX, wireframes, prototypes, user research, accessibility"
    }
}

MOTIVATION = [
    "Small progress every day creates big results.",
    "Your college assignments can become portfolio projects.",
    "You do not need to know everything; keep learning.",
    "Consistency matters more than one night of hard work.",
    "Build skills, not just certificates.",
    "Your beginning does not decide your ending."
]


def parse(text):
    aliases = {"ml": "machine learning", "js": "javascript",
               "powerbi": "power bi", "machinelearning": "machine learning"}
    return {aliases.get(x.strip().lower(), x.strip().lower())
            for x in text.split(",") if x.strip()}


def score(skills, interests, job, career):
    required = set(career["skills"].split())
    desired = set(career["interests"].split())
    skill = len(skills & required) / len(required) * 100
    interest = len(interests & desired) / len(interests | desired) * 100 if interests else 0
    job_score = 100 if job in ["Private Job", "Remote Job", "Freelancing"] else 0
    return round(float(np.clip(skill * .55 + interest * .35 + job_score * .10, 0, 100)), 1)


def set_text(widget, text):
    widget.config(state="normal")
    widget.delete("1.0", "end")
    widget.insert("end", text)
    widget.config(state="disabled")


root = tk.Tk()
root.title("Smart Skill Gap & Career Roadmap Analyzer")
root.geometry("1120x760")
root.configure(bg="#eef2ff")

style = ttk.Style()
style.theme_use("clam")

header = tk.Frame(root, bg="#243b80", pady=13)
header.pack(fill="x")
tk.Label(header, text="SMART CAREER ANALYZER", font=("Arial", 21, "bold"),
         bg="#243b80", fg="white").pack()
tk.Label(header, text="Find careers • Identify skill gaps • Plan your future",
         bg="#243b80", fg="white").pack()

main = tk.Frame(root, bg="#eef2ff")
main.pack(fill="both", expand=True, padx=12, pady=12)
left = tk.Frame(main, bg="white", padx=12, pady=10)
left.pack(side="left", fill="y", padx=(0, 10))
right = tk.Frame(main, bg="white", padx=8, pady=8)
right.pack(side="left", fill="both", expand=True)


def label(text):
    tk.Label(left, text=text, bg="white", font=("Arial", 9, "bold")).pack(anchor="w", pady=(7, 2))


def entry(default=""):
    e = ttk.Entry(left, width=32)
    e.pack(fill="x")
    e.insert(0, default)
    return e


label("Student Name")
name_entry = entry()
label("Skills (comma-separated)")
skills_entry = entry("python, excel, numpy")
label("Interests (comma-separated)")
interests_entry = entry("data, ai, coding, maths")
label("Preferred Job Type")
job_var = tk.StringVar(value="Private Job")
ttk.Combobox(left, textvariable=job_var, state="readonly",
             values=["Private Job", "Remote Job", "Freelancing"]).pack(fill="x")
label("Education")
edu_var = tk.StringVar(value="B.Tech")
ttk.Combobox(left, textvariable=edu_var, state="readonly",
             values=["Diploma", "B.Tech", "Graduate", "Postgraduate"]).pack(fill="x")
label("Daily Study Hours")
hours_var = tk.StringVar(value="3")
ttk.Combobox(left, textvariable=hours_var, state="readonly",
             values=["1", "2", "3", "4", "5", "6"]).pack(fill="x")
label("College Workload")
work_var = tk.StringVar(value="Normal")
ttk.Combobox(left, textvariable=work_var, state="readonly",
             values=["Light", "Normal", "Heavy / Exam Week"]).pack(fill="x")

notebook = ttk.Notebook(right)
notebook.pack(fill="both", expand=True)
outputs = {}
for tab in ["Dashboard", "Skill Gap", "Roadmap", "Study Planner", "Interviews", "Career Graph"]:
    frame = tk.Frame(notebook, bg="white")
    notebook.add(frame, text=tab)
    outputs[tab] = frame

textboxes = {}
for tab in ["Dashboard", "Skill Gap", "Roadmap", "Study Planner", "Interviews"]:
    textboxes[tab] = tk.Text(outputs[tab], wrap="word", font=("Arial", 10),
                             bg="#fbfcff", padx=10, pady=10, relief="flat")
    textboxes[tab].pack(fill="both", expand=True, padx=4, pady=4)
    textboxes[tab].config(state="disabled")

progress_tasks = []
completed = set()


def analyze():
    global progress_tasks
    skills, interests = parse(skills_entry.get()), parse(interests_entry.get())
    if not skills and not interests:
        messagebox.showwarning("Missing details", "Enter skills or interests.")
        return

    results = []
    for name, c in CAREERS.items():
        required = set(c["skills"].split())
        results.append((score(skills, interests, job_var.get(), c), name, c,
                        sorted(skills & required), sorted(required - skills)))
    results.sort(reverse=True, key=lambda x: x[0])
    best_score, best_name, best, matched, missing = results[0]
    student = name_entry.get().strip() or "Student"

    set_text(textboxes["Dashboard"],
        f"Welcome, {student}!\n\nTOP CAREER MATCHES\n\n" +
        "\n\n".join(f"{i}. {n} — {s}%\n{c['desc']}"
                    for i, (s, n, c, m, ms) in enumerate(results[:5], 1)) +
        f"\n\nBEST MATCH: {best_name} ({best_score}%)\n"
        f"Why consider it? {best['desc']}\n\n"
        "Scores compare your inputs with predefined profiles; they do not predict employment.")

    coverage = round(len(matched) / len(best["skills"].split()) * 100, 1)
    set_text(textboxes["Skill Gap"],
        f"SKILL GAP: {best_name}\nCurrent listed-skill coverage: {coverage}%\n\n"
        "SKILLS YOU LISTED\n" + ("\n".join("+ " + x for x in matched) or "No matching skills") +
        "\n\nSKILLS TO DEVELOP\n" + ("\n".join("- " + x for x in missing) or "All listed skills matched") +
        "\n\nHOW TO IMPROVE\n1. Learn one missing skill.\n2. Practice exercises.\n"
        "3. Use it in a mini project.\n4. Reassess your skills.\n"
        "This is a checklist, not a proficiency test.")

    progress_tasks = [phase for phase, topics, task in best["roadmap"]]
    completed.clear()
    roadmap = f"ROADMAP: {best_name}\n\n"
    for phase, topics, task in best["roadmap"]:
        roadmap += f"{phase}\nTopics: {topics}\nPractice: {task}\n\n"
    roadmap += "\nPROJECT IDEAS\n" + best["projects"]
    set_text(textboxes["Roadmap"], roadmap)

    hours = int(hours_var.get())
    workload = work_var.get()
    allocations = ([("College assignments and revision", .45), ("Career learning", .25),
                    ("DSA practice", .15), ("Projects", .05), ("Weekly review", .10)]
                   if workload == "Heavy / Exam Week" else
                   [("College assignments and revision", .20), ("Career learning", .30),
                    ("DSA practice", .20), ("Projects", .20), ("Weekly review", .10)]
                   if workload == "Light" else
                   [("College assignments and revision", .30), ("Career learning", .30),
                    ("DSA practice", .20), ("Projects", .12), ("Weekly review", .08)])
    plan = f"DAILY PLAN: {hours} hours | College workload: {workload}\n\n"
    plan += "\n".join(f"{task}: {round(hours * 60 * part)} minutes"
                      for task, part in allocations)
    plan += ("\n\nWEEKLY ROUTINE\nMonday: Learn topic + assignment\n"
             "Tuesday: Practice coding + DSA\nWednesday: College practical + revision\n"
             "Thursday: Project work\nFriday: Review + coding problems\n"
             "Saturday: GitHub and portfolio\nSunday: Revise and plan next week\n\n"
             "During exams, prioritize college deadlines and sleep.")
    set_text(textboxes["Study Planner"], plan)

    set_text(textboxes["Interviews"],
        f"INTERVIEW PREPARATION: {best_name}\n\n" +
        "\n".join(f"{i}. {topic}" for i, topic in enumerate(best["interview"].split(", "), 1)) +
        "\n\nPROJECT QUESTIONS\n- What problem does it solve?\n- Why these tools?\n"
        "- How did you test it?\n- What would you improve?\n\n"
        "Read entry-level job descriptions, maintain an honest resume and practice explaining your work.")

    for widget in outputs["Career Graph"].winfo_children():
        widget.destroy()
    top = results[:5]
    fig = Figure(figsize=(7, 5), dpi=100)
    ax = fig.add_subplot(111)
    bars = ax.barh([x[1] for x in top][::-1], [x[0] for x in top][::-1])
    ax.set_xlim(0, 110)
    ax.set_xlabel("Career Match (%)")
    ax.set_title("Top Five Career Matches")
    ax.grid(axis="x", alpha=.25)
    ax.bar_label(bars, fmt="%.1f%%", padding=3)
    fig.tight_layout()
    chart = FigureCanvasTkAgg(fig, master=outputs["Career Graph"])
    chart.draw()
    chart.get_tk_widget().pack(fill="both", expand=True)
    notebook.select(outputs["Dashboard"])


def checklist():
    if not progress_tasks:
        messagebox.showinfo("Analyze first", "Analyze your career first.")
        return
    win = tk.Toplevel(root)
    win.title("Roadmap Progress")
    win.geometry("560x420")
    variables = {}
    for task in progress_tasks:
        var = tk.BooleanVar(value=task in completed)
        variables[task] = var
        tk.Checkbutton(win, text=task, variable=var, wraplength=500,
                       anchor="w").pack(fill="x", padx=10, pady=4)

    def save():
        completed.clear()
        completed.update(task for task, var in variables.items() if var.get())
        messagebox.showinfo("Progress", f"{len(completed)}/{len(progress_tasks)} phases completed.")

    tk.Button(win, text="Save Progress", command=save, bg="#15976b",
              fg="white").pack(pady=12)


def motivation():
    messagebox.showinfo("Keep Going!",
        random.choice(MOTIVATION) +
        "\n\nAttend classes, complete assignments, practice coding, "
        "build projects and revise regularly. Your progress matters!")


for text, command, color in [
    ("ANALYZE MY CAREER", analyze, "#243b80"),
    ("ROADMAP CHECKLIST", checklist, "#15976b"),
    ("MOTIVATION & TIPS", motivation, "#7854c5")
]:
    tk.Button(left, text=text, command=command, bg=color, fg="white",
              font=("Arial", 9, "bold"), pady=8).pack(fill="x", pady=4)


def clear():
    for e in [name_entry, skills_entry, interests_entry]:
        e.delete(0, "end")
    skills_entry.insert(0, "")
    interests_entry.insert(0, "")
    job_var.set("Private Job")
    edu_var.set("B.Tech")
    hours_var.set("3")
    work_var.set("Normal")
    completed.clear()
    progress_tasks.clear()
    for box in textboxes.values():
        set_text(box, "Enter your details and click Analyze My Career.")
    for widget in outputs["Career Graph"].winfo_children():
        widget.destroy()


tk.Button(left, text="CLEAR FORM", command=clear, bg="#e5e9f8",
          fg="#243b80", pady=7).pack(fill="x", pady=4)

set_text(textboxes["Dashboard"],
         "Welcome!\nEnter your skills, interests and preferences, then analyze your career.\n\n" +
         random.choice(MOTIVATION))
root.mainloop()
