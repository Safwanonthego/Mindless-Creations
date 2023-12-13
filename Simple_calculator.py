print("What Mathematical Operation Do you want to Do?")
sys = input("Calc/Conv: ").upper()
if sys == "CALC":
    print("Calculator")
    x = int(input("Input X: "))
    y = int(input("Input y: "))
    
    print ("Choose operation")
    operator = input("A/S/M/D: ").upper()
    while operator not in ["A", "S", "M", "D"]:
        operator = input("A/S/M/D: ").upper()
    if operator == "A":
        print(f"Your answer: {x+y}" )
    elif operator == "S":
        print(f"Your answer: {x-y}" )
    elif operator == "M":
        print(f"Your answer: {x*y}" )
    elif operator == "D":
        print(f"Your answer: {x/y}" )
    
elif sys == "CONV":
    print("Conversion")
    print("Choose Conversation Method")
    conv_category = input("Length/Weight/BMI: ").upper()
    while conv_category not in ["LENGTH", "WEIGHT", "BMI"]:
        conv_category = input("Length/Weight/BMI/: ").upper()
        
    if conv_category == "LENGTH":
        x = float(input("Input value: "))
        unit_input = input("Input unit(m,yd,ft): ").lower()
        if unit_input == "m":
            unit_output = input("Input output(yd,ft): ").lower()
            if unit_output == "yd":
                print(f"{x*1.09} Yard")
            elif unit_output == "ft":
                print(f"{x*3.28} Foot")
            else:
                print ("Error") 
        elif unit_input == "yd":
           unit_output = input("Input output(m,ft): ").lower()
           if unit_output == "m":
               print(f"{x*0.91} Meter")
           elif unit_output == "ft":
                print(f"{x*3} Foot")
           else:
               print ("Error") 
        elif unit_input == "ft":
           unit_output = input("Input output(yd,m): ").lower()
           if unit_output == "yd":
               print(f"{x*0.33} Yard")
           elif unit_output == "m":
               print(f"{x*.03} Meter")
           else:
               print ("Error")                 
               
    elif conv_category == "WEIGHT":
        x = float(input("Input value: "))
        unit_input = input("Input unit(kg,t,lbs): ").lower()
        
        if unit_input == "kg":
            unit_output = input("Input output(t,lbs): ").lower()
            if unit_output == "t":
                print(f"{x*0.001} Metric Ton")
            elif unit_output == "lbs":
                print(f"{x*2.2} Pound")
            else:
                print ("Error") 
                
        elif unit_input == "t":
           unit_output = input("Input output(kg,lbs): ").lower()
           if unit_output == "kg":
               print(f"{x*1000} Kilogram")
           elif unit_output == "lbs":
                print(f"{x*2204.62} Pound")
           else:
               print ("Error") 
               
        elif unit_input == "lbs":
           unit_output = input("Input output(kg,t): ").lower()
           if unit_output == "kg":
               print(f"{x*0.45} kilogram")
           elif unit_output == "t":
               print(f"{x*0.000454} Metric Ton")
           else:
               print ("Error")               
         
    elif conv_category == "BMI":
        H_ft = float(input("Input Height (ft): "))
        H_in = float(input("Input Height (in): "))
        H_m = (H_ft * 0.3048 + H_in * 0.0254)
        W_kg = float(input("Input Weight (kg): "))
        bmi = W_kg/(H_m**2)
        if bmi < 18.5:
            print(f"BMI: {bmi}.\n Need to gain weight!")
        elif bmi < 24.9:
            print(f"BMI: {bmi}.\n You are Healthy!")
        elif bmi < 29.9:
            print(f"BMI: {bmi}.\n Loose some weight!")
        elif bmi > 30:
            print(f"BMI: {bmi}.\n You are at a risk!")        