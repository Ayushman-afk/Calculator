def run_calculator():

    while True:

        userinp = float(input("Enter Which Conversion You Would Like to do: \n 1. Length Conversions \n 2. Weight Conversions \n 3. Volume Conversions \n 4. Temperature Conversions \n 5. Quit \n Choice: "))

        if userinp == 1:
            length_conversion = float(input("Which Conversion Would You like to do for Length: \n 1. mm - cm \n 2. mm - m \n 3. mm - km \n 4. cm - mm \n 5. cm - m \n 6. cm - km \n 7. m - mm \n 8. m - cm \n 9. m - km \n 10. km - mm \n 11. km - cm \n 12. km - m \n Choice -  "))
            if length_conversion == 1:
                print("Picked mm - cm conversion")
                mm = float(input("Enter mm value: "))
                op = (mm) / (10)
                print("{}mm in cm is: {}cm".format(mm, op))

            elif length_conversion == 2:
                print("Picked mm - m conversion")
                mm = float(input("Enter mm value: "))
                op = (mm) / (1000)
                print("{}mm in m is: {}m".format(mm, op))

            elif length_conversion == 3:
                print("Picked mm - km conversion")
                mm = float(input("Enter mm value: "))
                op = (mm) / (1000000)
                print("{}mm in km is: {}km".format(mm, op))

            elif length_conversion == 4:
                print("Picked cm - mm conversion")
                cm = float(input("Enter cm value: "))
                op = (cm) * (10)
                print("{}cm in mm is: {}mm".format(cm, op))

            elif length_conversion == 5:
                print("Picked cm - m conversion")
                cm = float(input("Enter cm value: "))
                op = (cm) / (100)
                print("{}cm in m is: {}m".format(cm, op))

            elif length_conversion == 6:
                print("Picked cm - km conversion")
                cm = float(input("Enter cm value: "))
                op = (cm) / (100000)
                print("{}cm in km is: {}km".format(cm, op))

            elif length_conversion == 7:
                print("Picked m - mm conversion")
                m = float(input("Enter m value: "))
                op = (m) * (1000)
                print("{}m in mm is: {}mm".format(m, op))

            elif length_conversion == 8:
                print("Picked m - cm conversion")
                m = float(input("Enter m value: "))
                op = (m) * (100)
                print("{}m in cm is: {}cm".format(m, op))

            elif length_conversion == 9:
                print("Picked m - km conversion")
                m = float(input("Enter m value: "))
                op = (m) / (1000)
                print("{}m in km is: {}km".format(m, op))

            elif length_conversion == 10:
                print("Picked km - mm conversion")
                km = float(input("Enter km value: "))
                op = (km) * (1000000)
                print("{}km in mm is: {}mm".format(km, op))

            elif length_conversion == 11:
                print("Picked km - cm conversion")
                km = float(input("Enter km value: "))
                op = (km) * (100000)
                print("{}km in cm is: {}cm".format(km, op))

            elif length_conversion == 12:
                print("Picked km - m conversion")
                km = float(input("Enter km value: "))
                op = (km) * (1000)
                print("{}km in m is: {}m".format(km, op))
            else:
                print("Invalid Choice")

        elif userinp == 2:
            weight_conversion = float(input("Enter which weight conversions you would like to do: \n 1. g - kg \n 2. g - lb \n 3. g - oz \n 4. kg - g \n 5. kg - lb \n 6. kg - oz \n 7. lb - g \n 8. lb - kg \n 9. lb - oz \n 10. oz - g \n 11. oz - kg \n 12. oz - lb \n Choice -  "))
            if weight_conversion == 1:
                print("Picked g - kg conversion")
                g = float(input("Enter g value: "))
                op = (g) / 1000
                print("{}g in kg is: {}kg".format(g, op))

            elif weight_conversion == 2:
                print("Picked g - lb conversion")
                g = float(input("Enter g value: "))
                op = (g) / 453.592
                print("{}g in lb is: {:.2f}lb".format(g, op))

            elif weight_conversion == 3:
                print("Picked g - oz conversion")
                g = float(input("Enter g value: "))
                op = (g) / 28.3495
                print("{}g in oz is: {:.2f}oz".format(g, op))

            elif weight_conversion == 4:
                print("Picked kg - g conversion")
                kg = float(input("Enter kg value: "))
                op = (kg) * 1000
                print("{}kg in g is: {}g".format(kg, op))

            elif weight_conversion == 5:
                print("Picked kg - lb conversion")
                kg = float(input("Enter kg value: "))
                op = (kg) * 2.20462
                print("{}kg in lb is: {:.2f}lb".format(kg, op))

            elif weight_conversion == 6:
                print("Picked kg - oz conversion")
                kg = float(input("Enter kg value: "))
                op = (kg) * 35.274
                print("{}kg in oz is: {:.2f}oz".format(kg, op))

            elif weight_conversion == 7:
                print("Picked lb - g conversion")
                lb = float(input("Enter lb value: "))
                op = (lb) * 453.592
                print("{}lb in g is: {:.2f}g".format(lb, op))

            elif weight_conversion == 8:
                print("Picked lb - kg conversion")
                lb = float(input("Enter lb value: "))
                op = (lb) * 0.453592
                print("{}lb in kg is: {:.2f}kg".format(lb, op))

            elif weight_conversion == 9:
                print("Picked lb - oz conversion")
                lb = float(input("Enter lb value: "))
                op = (lb) * 16
                print("{}lb in oz is: {:.2f}oz".format(lb, op))

            elif weight_conversion == 10:
                print("Picked oz - g conversion")
                oz = float(input("Enter oz value: "))
                op = (oz) * 28.3495
                print("{}oz in g is: {:.2f}g".format(oz, op))

            elif weight_conversion == 11:
                print("Picked oz - kg conversion")
                oz = float(input("Enter oz value: "))
                op = (oz) * 0.0283495
                print("{}oz in kg is: {:.4f}kg".format(oz, op))

            elif weight_conversion == 12:
                print("Picked oz - lb conversion")
                oz = float(input("Enter oz value: "))
                op = (oz) / 16
                print("{}oz in lb is: {:.2f}lb".format(oz, op))
            else:
                print("Invalid Choice")

        elif userinp == 3:
            volume_conversions = float(input("Enter which volume conversion you would like to do: \n 1. ml - l \n 2. ml - cup \n 3. ml - gallon \n 4. l - ml \n 5. l - cup \n 6. l - gallon \n 7. cup - ml \n 8. cup - l \n 9. cup - gallon \n 10. gallon - ml \n 11. gallon - l \n 12. gallon - cup \n Choice -  "))
            if volume_conversions == 1:
                print("Picked ml - l conversion")
                ml = float(input("Enter ml value: "))
                op = (ml) / 1000
                print("{}ml in l is: {}l".format(ml, op))

            elif volume_conversions == 2:
                print("Picked ml - cup conversion")
                ml = float(input("Enter ml value: "))
                op = (ml) / 236.588
                print("{}ml in cup is: {}cup(s)".format(ml, op))

            elif volume_conversions == 3:
                print("Picked ml - gallon conversion")
                ml = float(input("Enter ml value: "))
                op = (ml) / 3785.41
                print("{}ml in gallon is: {}gallon".format(ml, op))

            elif volume_conversions == 4:
                print("Picked l - ml conversion")
                l = float(input("Enter l value: "))
                op = (l) * 1000
                print("{}l in ml is: {}ml".format(l, op))

            elif volume_conversions == 5:
                print("Picked l - cup conversion")
                l = float(input("Enter l value: "))
                op = (l) * 4.22675
                print("{}l in cup is: {}cup(s)".format(l, op))

            elif volume_conversions == 6:
                print("Picked l - gallon conversion")
                l = float(input("Enter l value: "))
                op = (l) / 3.78541
                print("{}l in gallon is: {}gallon".format(l, op))

            elif volume_conversions == 7:
                print("Picked cup - ml conversion")
                cup = float(input("Enter cup value: "))
                op = (cup) * 236.588
                print("{}cup in ml is: {}ml".format(cup, op))

            elif volume_conversions == 8:
                print("Picked cup - l conversion")
                cup = float(input("Enter cup value: "))
                op = cup * 0.236588
                print("{}cup in l is: {}l".format(cup, op))

            elif volume_conversions == 9:
                print("Picked cup - gallon conversion")
                cup = float(input("Enter cup value: "))
                op = (cup) / 16
                print("{}cup in gallon is: {}gallon".format(cup, op))

            elif volume_conversions == 10:
                print("Picked gallon - ml conversion")
                gallon = float(input("Enter gallon value: "))
                op = (gallon) * 3785.41
                print("{}gallon in ml is: {}ml".format(gallon, op))

            elif volume_conversions == 11:
                print("Picked gallon - l conversion")
                gallon = float(input("Enter gallon value: "))
                op = (gallon) * 3.78541
                print("{}gallon in l is: {}l".format(gallon, op))

            elif volume_conversions == 12:
                print("Picked gallon - cup conversion")
                gallon = float(input("Enter gallon value: "))
                op = (gallon) * 16
                print("{}gallon in cup is: {}cup(s)".format(gallon, op))
            else:
                print("Invalid Choice")

        elif userinp == 4:
            temp_conversions = float(input("Enter what temp conversion you would like to do: \n 1.  c - f \n 2.  c - k \n 3.  f - c \n 4. f - k \n 5. k - c \n 6. k - f \n Choice -  "))

            if temp_conversions == 1:
                print("Picked c - f conversion")
                c  = float(input("Enter c value: "))
                op = (c) * (9/5) + 32
                print("{}celsius in fahrenheit is: {}fahreinheit".format(c, op))

            elif temp_conversions == 2:
                print("Picked c - k conversion")
                c = float(input("Enter c value: "))
                op = (c) + 273.15
                print("{}celsius in kelvin is: {}kelvin".format(c, op))

            elif temp_conversions == 3:
                print("Picked f - c conversion")
                f = float(input("Enter f value: "))
                op = ((f) - 32) * (5/9)
                print("{}fahreinheit in celsius is: {}celsius".format(f, op))

            elif temp_conversions == 4:
                print("Picked f - k conversion")
                f = float(input("Enter f value: "))
                op = ((f) - 32) * (5/9) + 273.15
                print("{}fahreinheit in kelvin is: {}kelvin".format(f, op))

            elif temp_conversions == 5:
                print("Picked k - c conversion")
                k = float(input("Enter k value: "))
                op = (k) - 273.15
                print("{}kelvin in celsius is: {}celsius".format(k, op))

            elif temp_conversions == 6:
                print("Picked k - f conversion")
                k = float(input("Enter k value: "))
                op = ((k) - 273.15) * (9/5) + 32
                print("{}kelvin in fahreinheit is: {}fareinheit".format(k, op))
            else:
                print("Invalid Choice")

        elif userinp == 5:
            break

if __name__ == "__main__":
    run_calculator()