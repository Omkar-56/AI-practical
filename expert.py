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