import json 

def applicant_score(applicant, team_avg_attributes):
    total_attributes = len(applicant["attributes"])
    score = sum((min(applicant["attributes"][attr], team_avg_attributes[attr])) / (max(applicant["attributes"][attr], team_avg_attributes[attr])) for attr in applicant["attributes"])
    return score / total_attributes

def team_averages(applicants, team): #calculates averages of team's attributes 
    team_avg_attributes = {attr: sum(member["attributes"][attr] for member in team) / len(team) for attr in team[0]["attributes"]} 
    scored_applicants = []
    for applicant in applicants:
        average_score = applicant_score(applicant, team_avg_attributes)
        scored_applicants.append({"name": applicant["name"], "score": round(average_score, 2)})
    return {"scoredApplicants": scored_applicants}

def main():
    input_data = '''
    {
        "team": [
            {"name": "Eddie", "attributes": {"intelligence": 1, "strength": 5, "endurance": 3, "spicyFoodTolerance": 1}},
            {"name": "Will", "attributes": {"intelligence": 9, "strength": 4, "endurance": 1, "spicyFoodTolerance": 6}},
            {"name": "Mike", "attributes": {"intelligence": 3, "strength": 2, "endurance": 9, "spicyFoodTolerance": 5}}
        ],
        "applicants": [
            {"name": "John", "attributes": {"intelligence": 4, "strength": 5, "endurance": 2, "spicyFoodTolerance": 1}},
            {"name": "Jane", "attributes": {"intelligence": 7, "strength": 4, "endurance": 3, "spicyFoodTolerance": 2}},
            {"name": "Joe", "attributes": {"intelligence": 1, "strength": 1, "endurance": 1, "spicyFoodTolerance": 10}}
        ]
    }
    '''
    data = json.loads(input_data)
    result = team_averages(data["applicants"], data["team"])
    output_data = json.dumps(result, indent=2)
    print(output_data)

if __name__ == "__main__":
    main()