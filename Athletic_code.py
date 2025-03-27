def get_skating_advice(element, issue): 
    coaching_tips = { 
        'axel': {
            "height": "Make sure to bend your knees deeply on your takeoff leg and feel like you're rising to the top of your toepick with power.", 
            "unstable": "Engage your core and check your free leg. Make sure to have your leg in eagle when you land before you come out.", 
            "over rotation": "Ensure you are always jumping to the outside of your circle."
        }, 
        'salchow': { 
            'underrotation': "Check your arms before bringing them in quickly and maintain a tight air position.", 
            'slipping': "Ensure you enter on a strong deep inside edge with your weight centered over your skating foot.", 
            'takeoff': "Focus on a strong knee bend and an explosive push from the skating leg. Think about the jump; some tips would be to practice off-ice."
        }, 
        'toe loop': { 
            'toe pick': "If you are not placing the toe pick properly, this can cause a lot of issues in the jump. Ensure you are digging the toepick backward before you turn forward and push straight forward, not back.", 
            'toepick': "If you are not placing the toe pick properly, this can cause a lot of issues in the jump. Ensure you are digging the toepick backward before you turn forward and push straight forward, not back.",
            'swinging': "Instead of swinging your leg back on the takeoff, you should focus on bringing it straight back. Practice off-ice rotational drills.", 
            'around corner': "Instead of swinging your leg back on the takeoff, you should focus on bringing it straight back. Practice off-ice rotational drills.",
            'toeaxeling': "Keep your shoulders and hips aligned backward before takeoff. You should practice slow walkthroughs beside the boards or off-ice to fix this."
        },
        'loop': { 
            'free foot': "Practice jumping off only that foot off-ice. You should focus on having pressure and your weight only on your takeoff foot and not your free leg. However, always be conscious of where the free leg is.", 
            'toe assisting': "Practice jumping off only that foot off-ice. You should focus on having pressure and your weight only on your takeoff foot and not your free leg. However, always be conscious of where the free leg is.", 
            'leaning': "Bend your knee deeper during takeoff to create more power. You can practice off-ice squats or single-leg jumps. Ensure your ankles are crossed tightly together.", 
            'wobbly': "Bend your knee deeper during takeoff to create more power. You can practice off-ice squats or single-leg jumps. Ensure your ankles are crossed tightly together."
        }, 
        'flip': { 
            'takeoff edge': "Try following your flip on a circle to enforce the deep inside edge, ensuring that is where you apply your weight. Practice a slow walkthrough by the boards of the takeoff.", 
            'flutzing': "Try following your flip on a circle to enforce the deep inside edge, ensuring that is where you apply your weight. Practice a slow walkthrough by the boards of the takeoff.",
            'leaning': "Ensure your head is looking to the inside of the circle and that you are leaning slightly forward. Keep your core engaged throughout the whole jump. Practice core exercises.", 
            'uncontrolled': "Ensure your head is looking to the inside of the circle and that you are leaning slightly forward. Keep your core engaged throughout the whole jump. Practice core exercises.", 
            'swinging': "The free leg should move straight through, not around. You should be able to have a direct knee lift, making an 'h' shape at the beginning of the jump. Practice off-ice rotational jumps or waltz jump snaps.", 
            'free leg': "The free leg should move straight through, not around. You should be able to have a direct knee lift, making an 'h' shape at the beginning of the jump. Practice off-ice rotational jumps or waltz jump snaps."
        },
        'lutz': { 
            'takeoff edge': "Practice controlled drills of specifically feeling that deep outside edge. Exaggerate the outside edge. Focus on the edge before putting your toe in. Outside rockers are a useful exercise.", 
            'weak': "Ensure your toe pick digs into the ice firmly, and use explosive power from the picking foot to jump higher. Always focus on first jumping upwards; the distance will come with practice."
        }, 
        'sit spin': { 
            'falling over': "Keep your weight over your skating leg and engage your core more. Try focusing on the tip of your fingers as you spin.",
            'losing balance': "Keep your weight over your skating leg and engage your core more. Try focusing on the tip of your fingers as you spin.",
            'centering': "Focus on keeping every part of your body aligned. Head looking forward, arms in front. Practice holding the position outside of the spin first."
        }, 
        'camel spin': { 
            'slow': "Push harder into the entry edge and keep your knee bent until you have reached that spin pivot point. Engage your core.", 
            'speed': "Push harder into the entry edge and keep your knee bent until you have reached that spin pivot point. Engage your core.", 
            'balance': "Ensure your head is aligned, keep gaze forward and slightly down. Also ensure your hips are aligned with the shoulders. The body should be a straight line.", 
            'uneven': "Ensure your head is aligned, keep gaze forward and slightly down. Also ensure your hips are aligned with the shoulders. The body should be a straight line."
        }, 
        'backspin': { 
            'slow': "Ensure to apply pressure to your arms and your free leg and pull them in very fast when starting the spin.", 
            'no speed': "Ensure to apply pressure to your arms and your free leg and pull them in very fast when starting the spin.", 
            'wobbly': "Keep your head steady and ensure that you apply pressure to your free leg when exiting. Ensure your body is aligned and fully engaged. Focus on one point.", 
            'falling': "Keep your head steady and ensure that you apply pressure to your free leg when exiting. Ensure your body is aligned and fully engaged. Focus on one point."
        }
    }

    element = element.lower()
    issue = issue.lower()

    if element in coaching_tips:
        for key in coaching_tips[element]:
            if key in issue:
                return coaching_tips[element][key]
        return "I don't have advice for that specific issue at this moment. Try describing it differently!"
    else:
        return "Sorry, that element does not seem to be in our database. Try another one!"

def main(): 
    print("Welcome to SkateBot: The AI-powered Figure Skating Coach!")

    while True: 
        element = input('\nEnter the figure skating element you are working on currently or type exit to quit: ').strip()
        if element.lower() == "exit": 
            print("Good luck with the rest of your training! Hope to see you again!")
            break 

        issue = input("Describe the issue you are facing with your element: ").strip()
        advice = get_skating_advice(element, issue)

        print('\nCoaching Advice: ')
        print(advice)

if __name__ == "__main__": 
    main()
