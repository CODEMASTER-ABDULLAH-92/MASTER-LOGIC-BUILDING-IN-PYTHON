# Take a temperature value and print “Cold” “Warm”

# | Temperature (°C) | Description |
# | ---------------: | ----------- |
# |    Below **0°C** | Freezing ❄️ |
# |   **0°C – 10°C** | Very Cold   |
# |  **11°C – 20°C** | Cool        |
# |  **21°C – 25°C** | Warm        |
# |  **26°C – 30°C** | Hot         |
# |   **Above 30°C** | Very Hot 🔥 |

temp = int(input("Enter the temp value: "))

if temp < 0:
    print("Freezing: ")
elif temp >= 0 and temp <= 10:
    print("Very Cold")
elif temp >= 11 and temp <=20:
    print("Cool")
elif temp >= 21 and temp <=25:
    print("Warm")
elif temp >= 26 and temp <= 30:
    print("Hot")
else:
    print("Very Hot")


# =================================
# Same and Simple approach 
# =================================

# if temp < 0:
#     print("Freezing")
# elif temp <= 10:
#     print("Very Cold")
# elif temp <= 20:
#     print("Cool")
# elif temp <= 25:
#     print("Warm")
# elif temp <= 30:
#     print("Hot")
# else:
#     print("Very Hot")