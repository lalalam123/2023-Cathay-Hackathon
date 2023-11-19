# Notice that the demo version will show pre-selected result to avoid unstable situation during presentation
import tkinter as tk
import time
import requests
import json

# Please do not zero day attack us
# Notice that the apiKey and secretKey will be expired at the end of the 2023 Cathay Hackathon
apikey= "p7GSSg9KGsKuS8mapCN8iLxj"
secretkey = "6yO5kvKkfUi7ZExO4WsHw72SyUG8CkW5"

def get_access_token():
    """
    使用 API Key，Secret Key 获取access_token，替换下列示例中的应用API Key、应用Secret Key
    """
        
    url = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={apikey}&client_secret={secretkey}"
    
    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json().get("access_token")

# Function to fetch data from the API
def request(prompt, demo):
    # Perform API request here
    # Replace the following line with your API request code

    # Display the response
    text_area.delete(1.0, tk.END)
    for i, message in enumerate([str1, str2, str3, str4, str5]):

        if i % 2 == 0:
            gpt = "GPT No.1: "
        else:
            gpt = "GPT No.2: "

        lastres = "This is a long message that will take a while to display."

        if demo == True:
            text_area.insert(tk.END, gpt + message + '\n\n')
            time.sleep(2)  # Delay between messages
            root.update()
        else:
            payload = json.dumps({
            "messages": [
                {
                    "role": "user",
                    "content": f"{prompt}"
                }
            ]
            })
            headers = {
                'Content-Type': 'application/json'
            }
            url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions?access_token=" + get_access_token()
            response = requests.request("POST", url, headers=headers, data=payload)
            response = str(response.json()['result'])
            prompt =  response
            text_area.insert(tk.END, gpt + response + '\n\n')
            root.update()

        

# Backup Text Prompt Demonstration in case of any accident on the API request
str1 = "The human customer ask, Can we utilize cyclic weather pattern to develop seasonal multi-dimensional routes to reduce fuel consumption? such as Hong Kong to Taipei, Taipei to Japan, Japan to Hong Kong. Let me elaborate more about it, I want you to help search for the best machine learning models and correlated data to analysis the prediction and give me some insight on it...\n"
str2 = "Yes, boss. In terms of data, I am going to collect the air pressure, temperature, wind direction, wind strength, flight fuel consumption, flight carbon emission. In terms of model, I am going to use multi-models to do the analysis, included but not limited to decision tree, genetic algorithm, gaussian logistic, regression model, neuron network, ... The result of the analysis is that ...\n"
str3 = "It's great, but you seems have missed the consideration of freedom of air, risk diversification, and the impact of the weather on the flight safety."
str4 = "Yes, mum. I will take them into consideration. I will also consider the impact of the weather on the flight safety. I will fix the analysis model by adding the risk diversification model and the impact of the weather on the flight safety. The result of the analysis is that ...\n"
str5 = "OK, it's great. I will summarize your report and send it to our loyal human customer:\n\nWind Optimal Flight Trajectories within a 3 dimensional flight network can achieve a potential 1% to 10% fuel saving in a multi-dimensional flight by constructing wind optimal path\n\nWe can utilize headwind to generate more lifts to reduce takeoff distance and fuel consumption\n\nAlso, we can consider developing seasonal routes with an afforable prize and attract more customer, which also develop a sustainable economy."

# Function to handle button click event
def on_button_click():
    prompt = input_field.get().strip()
    if not prompt:
        return
    print(prompt)
    request(prompt, demo=True)

# Create the main window
root = tk.Tk()
root.attributes('-fullscreen', True)

# Create the text input field
input_field = tk.Entry(root, font=('Arial', 50))
input_field.grid(row=1, column=0, sticky='ew')

# Create the submit button
submit_button = tk.Button(root, text='Submit', command=on_button_click, font=('Arial', 50))
submit_button.grid(row=1, column=1, sticky='ew')

# Create the text area for displaying the response
text_area = tk.Text(root, font=('Arial', 50))
text_area.grid(row=0, column=0, columnspan=2, sticky='nsew')

# Configure the grid to expand properly when the window is resized
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Start the main loop
root.mainloop()