def analyze_resume(resume, job_description):
    resume_words = set(resume.lower().split())
    job_words = set(job_description.lower().split())

    important_words = {
        word for word in job_words
        if len(word) > 4
    }

    matched = resume_words.intersection(important_words)
    missing = important_words - resume_words

    if important_words:
        score = int((len(matched) / len(important_words)) * 100)
    else:
        score = 0

    print("\n--- AI Resume Analyzer ---")
    print(f"Resume Match Score: {score}%")

    print("\nMatched Keywords:")
    for word in sorted(matched):
        print(f"- {word}")

    print("\nPotential Missing Keywords:")
    for word in sorted(missing):
        print(f"- {word}")

    if score >= 70:
        print("\nGood match! 🚀")
    elif score >= 40:
        print("\nYour resume could be improved. 💡")
    else:
        print("\nConsider adding more relevant skills and keywords. 📝")


print("📄 AI Resume Analyzer")
print("---------------------")

resume = input("Paste your resume text: ")

job_description = input("\nPaste the job description: ")

analyze_resume(resume, job_description)
