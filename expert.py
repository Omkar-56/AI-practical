# Assignment-C6 (Expert System)

def evaluate_employee():
    print("🔍 Employee Performance Evaluation System\n")

    # Input section
    attendance = input("1. Attendance (Good / Average / Poor): ").strip().lower()
    project = input("2. Project Completion (On Time / Delayed / Incomplete): ").strip().lower()
    teamwork = input("3. Teamwork (Excellent / Good / Poor): ").strip().lower()
    punctuality = input("4. Punctuality (Always on time / Often late): ").strip().lower()

    # Score system
    score = 0

    # Attendance score
    if attendance == "good":
        score += 3
    elif attendance == "average":
        score += 2
    elif attendance == "poor":
        score += 0

    # Project completion score
    if project == "on time":
        score += 3
    elif project == "delayed":
        score += 1
    elif project == "incomplete":
        score += 0

    # Teamwork score
    if teamwork == "excellent":
        score += 3
    elif teamwork == "good":
        score += 2
    elif teamwork == "poor":
        score += 0

    # Punctuality score
    if punctuality == "always on time":
        score += 2
    elif punctuality == "often late":
        score += 0

    # Decision logic
    print("\n📊 Evaluation Result:",score)
    
    if score >= 9:
        print("⭐ Performance: Excellent")
    elif score >= 6:
        print("✅ Performance: Good")
    elif score >= 3:
        print("⚠️ Performance: Needs Improvement")
    else:
        print("❌ Performance: Poor")

# Run the expert system
evaluate_employee()


def evaluate_performance(employee):
    performance = []
    
    # Rules for evaluation
    if employee["projects_completed"] >= 10:
        performance.append("Outstanding contribution in project completion.")
    elif employee["projects_completed"] >= 5:
        performance.append("Good performance in project completion.")
    else:
        performance.append("Needs improvement in project completion.")

    if employee["average_rating"] >= 4.5:
        performance.append("Highly rated by peers and clients.")
    elif employee["average_rating"] >= 3.5:
        performance.append("Satisfactory rating from peers and clients.")
    else:
        performance.append("Low rating from peers and clients.")

    if employee["working_hours"] > 45:
        performance.append("Shows dedication but needs better time management.")
    elif 35 <= employee["working_hours"] <= 45:
        performance.append("Excellent time management skills.")
    else:
        performance.append("Needs to improve time management.")

    if employee["leadership_skills"] == "yes":
        performance.append("Exhibits strong leadership skills.")

    return performance

def main():
    # Collecting employee details
    print("Enter employee details:")
    name = input("Name: ")
    projects_completed = int(input("Number of projects completed: "))
    average_rating = float(input("Average performance rating (out of 5): "))
    working_hours = int(input("Weekly working hours: "))
    leadership_skills = input("Leadership skills (yes/no): ").strip().lower()

    # Create employee record
    employee = {
        "name": name,
        "projects_completed": projects_completed,
        "average_rating": average_rating,
        "working_hours": working_hours,
        "leadership_skills": leadership_skills
    }

    # Evaluate employee performance
    performance = evaluate_performance(employee)

    # Display results
    print(f"\nPerformance Evaluation for {name}:")
    for aspect in performance:
        print(f"- {aspect}")

if _name_ == "_main_":
    main()

def info_management():
    print("Information Management Expert System\n")

    data_type = input("1. Data Type (Structured / Unstructured): ").strip().lower()
    sensitivity = input("2. Sensitivity Level (High / Medium / Low): ").strip().lower()
    access_frequency = input("3. Access Frequency (High / Low): ").strip().lower()

    print("\nRecommendation:")
    if data_type == "structured":
        if sensitivity == "high":
            print("Use encrypted relational database with role-based access.")
        elif access_frequency == "high":
            print("Use high-performance database with indexing.")
        else:
            print("Use standard relational database.")
    elif data_type == "unstructured":
        if sensitivity == "high":
            print("Store in secure document management system with encryption.")
        elif access_frequency == "low":
            print("Use long-term cloud storage with cold access.")
        else:
            print("Use a content management system with search capabilities.")
    else:
        print("Invalid input. Please classify data properly.")

info_management()

def diagnose_patient():
    print("Medical Diagnosis Expert System\n")

    symptom1 = input("1. Primary Symptom (Fever / Chest Pain / Headache / Rash): ").strip().lower()
    symptom2 = input("2. Secondary Symptom (Cough / Breathlessness / Light Sensitivity / Itching): ").strip().lower()

    print("\nDiagnosis:")
    if symptom1 == "fever" and symptom2 == "cough":
        print("Likely Flu. Recommend rest and fluids.")
    elif symptom1 == "chest pain" and symptom2 == "breathlessness":
        print("Possible Heart Issue. Immediate ECG advised.")
    elif symptom1 == "headache" and symptom2 == "light sensitivity":
        print("Possible Migraine. Reduce light exposure.")
    elif symptom1 == "rash" and symptom2 == "itching":
        print("Allergic Reaction. Antihistamine recommended.")
    else:
        print("Unable to diagnose. Further examination required.")

diagnose_patient()

def helpdesk_support():
    print("Help Desk Expert System\n")

    issue = input("1. Issue Type (Login / Software / Network / Printer): ").strip().lower()
    urgency = input("2. Urgency Level (High / Medium / Low): ").strip().lower()

    print("\nSuggested Action:")
    if issue == "login":
        if urgency == "high":
            print("Immediate password reset via admin portal.")
        else:
            print("Guide user through self-service password reset.")
    elif issue == "software":
        print("Check for updates or reinstall the software.")
    elif issue == "network":
        print("Check router, restart modem, and verify connections.")
    elif issue == "printer":
        print("Check paper, ink, and reinstall drivers if needed.")
    else:
        print("Unrecognized issue. Escalate to Tier 2 support.")

helpdesk_support()

def stock_advisor():
    print("Stock Market Expert System\n")

    trend = input("1. Market Trend (Up / Down / Flat): ").strip().lower()
    volume = input("2. Trade Volume (High / Low): ").strip().lower()
    sentiment = input("3. News Sentiment (Positive / Neutral / Negative): ").strip().lower()

    print("\nRecommendation:")
    if trend == "up" and volume == "high" and sentiment == "positive":
        print("Buy")
    elif trend == "down" and volume == "high" and sentiment == "negative":
        print("Sell")
    elif trend == "flat" or sentiment == "neutral":
        print("Hold")
    else:
        print("Market uncertain. Wait for clearer signals.")

stock_advisor()

def airline_scheduler():
    print("Airline Scheduling Expert System\n")

    cargo_weight = int(input("1. Cargo Weight in kg: ").strip())
    route = input("2. Route Type (Domestic / International): ").strip().lower()
    urgency = input("3. Urgency (High / Low): ").strip().lower()

    print("\nAircraft Assignment:")
    if cargo_weight > 10000 and route == "international":
        print("Assign Cargo Aircraft A - Heavy-duty hauler.")
    elif cargo_weight <= 1000 and route == "domestic":
        print("Assign Small Jet B - Light domestic cargo.")
    elif 1000 < cargo_weight <= 10000:
        print("Assign Medium Hauler C - Standard freight.")
    elif urgency == "high":
        print("Assign Fast Transport Jet D - Urgent delivery.")
    else:
        print("Manual scheduling recommended for review.")

airline_scheduler()
