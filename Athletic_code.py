def get_skating_advice(elements, issue): 
    coaching_tips= { 
        'axel': {
            if "height" in issue: "Make sure to bend your knees deeply on the your takeoff leg and feel like your rising to the top of your toepick with power.", 
            if "unstable" in issue: "Engage your care and check your free leg, make sure to have your leg in eagle when you land before you come out.", 
            if "over rotation" in issue: "Ensure your are always jumping to the outside of your circle."
        }, 
        'salchow': { 
            if 'underrotation' in issue: "Check your arms before bringing them in quickly and maintain a tight air position.", 
            if 'slipping' in issue: "Ensure you enter on a strong deep inside edge with your weight centered over your skating foot.", 
            if 'takeoff' in issue: "Focus on a strong knee bend and an explosive push from the skating legl. Think about the jump, some tips would be to practice off-ice."
        }, 
        'sit spin': { 
            if 'falling over' or 'losing balance' in issue: "Keep your weight over your skating leg and engage your core more. Try focusing on the tip of your fingers as you spin.",
            if 'centering' in issue: "Focus on keeping every part of your body aligned. Head looking forward, arms in front. Practice holding the position outside of the spin first."
        }, 
        'camel spin': { 
            if 'slow' or 'speed' in issue: "Push harder into the entry edge and keep your knee bent until you have reached that spin pvivot point. Engage your core.", 
            if 'balance' ir 'uneven' in issue: "Ensure your head is aligned, keep gaze forward and slightly down. Also ensure your hips are aligned with the shoulders. Body should be a straight line."
        }
    }

    element = element.lower()
    issue = issue.lower()

    if element in coaching_tips and issue in coaching_tips[elements]: 
        return coaching_tips[elements][issue]
    elif element not in coaching_tips: 
        return "Sorry, that elemnt does not seem to be in our database. Sorry for the inconvenience, try another one!"
    else: 
        return "I don't have advice for that specific issue at this moment. Try describing it differently!"


def main(): 
    print("Welcome to SkateBot: The AI powered Figure Skating Coach!")

    while True: 
        element = input('\nEnter the figure skating element you are working on currently or type exit to quit: ').strip()
        if element.lower()=="exit": 
            print("Good luck with the rest of your training! Hope to see you again!")
            break; 

        issue = input("Describe the issue you are facing with your element: ").strip()
        advice = get_skating_advice(element, issue)

        print('\nCoaching Advice: ')
        print(advice)

if __name__ =="__main__": 
    main()