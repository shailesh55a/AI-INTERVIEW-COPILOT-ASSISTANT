import streamlit as st

# Import all modules
from src.resume_parser import extract_text
from src.resume_analyzer import analyze_resume
from src.jd_matcher import match_resume_jd
from src.question_generator import generate_questions
from src.answer_evaluator import evaluate_answer
from src.database import init_db, save_interview
from src.report_generator import generate_report
 # initialize database at startup
init_db()

# page configuration

st.set_page_config(
    page_title="AI Interview Copilot",
    page_icon="🧠",
    layout="wide"
)

# appliaction title
st.title("🧠 AI Interview Copilot")
st.write("Upload your resume, compare it with a Job Description, and practice interviews using AI.")

# resume upload

resume_file = st.file_uploader(
    "📄 Upload Resume (PDF)",
    type=["pdf"]
)

# job description input
jd = st.text_area(
    "📋 Paste Job Description",
    height=200
)

# main processing
if resume_file and jd:

    # Extract text from uploaded resume pdf
    resume_text = extract_text(resume_file)

    st.success("✅ Resume uploaded successfully")

    # resume analysis section

    st.header("📄 Resume Analysis")

    with st.spinner("Anlyzing Resume..."):
        resume_analysis = analyze_resume(resume_text)

    st.write(resume_analysis)

    # jd matching section
    st.header("🎯 Resume vs JD Match")

    with st.spinner("Comparing Resume with Job Description..."):
        match_result = match_resume_jd(resume_text, jd)

    st.write(match_result)

    # interview questions section

    st.header("❓ AI Generated Interview Questions")

    with st.spinner("Generating Questions..."):
        questions = generate_questions(resume_text, jd)

    st.write(questions)

    # practice interview section

    st.header("💬 Practice Interview")

    name = st.text_input("Candidate Name", "candidate")

    question = st.text_input(
        "Enter an interview Question"
    )

    answer = st.text_area(
        "Write Your Answer",
        height=150
    )

    # evaluate_answer

    if st.button("🚀 Evaluate Answer"):

        # Validate input
        if not question:
            st.warning("Please enter a question.")
        elif not answer:
            st.warning("Please enter an answer.")
        else:

            with st.spinner("Evaluating Answer..."):

                # get evaluation
                evaluation_result = evaluate_answer(
                    question,
                    answer
                )

            # display evaluation
            st.subheader("📊 Evaluation Result")
            st.write(evaluation_result)

            # Generating pdf report
            report_path = generate_report(
                name if name else "candidate",
                evaluation_result
            )

            # save result in database
            save_interview(
                name if name else "candidate",
                "Generated Score",
                evaluation_result
            )

            st.success("✅ Interview Report Generated")

            # show report location
            st.info(f"PDF saved at :{report_path}")

# footer
st.markdown("---")
st.caption("AI Interview Copilot | Groq + streamlit + SQLit + Reportlab")