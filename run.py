from tkinter import*
from fabrics import fabrics

#main window
window=Tk()
window.title("Fabric Sustainability Analyzer")
window.geometry("700x600")
window.config(bg="#9FF3A6")

#functions
def analyze_fabric():
    fabric = fabric_var.get()

    if fabric == "Select a Fabric Type":
        result_show.config(text="Please select a Fabric Type")
        return

    data = fabrics[fabric] #saving fabrics info in data var

    result_text = f"""
👕Fabric: {fabric}  

♻️ Carbon Footprint: {data['carbon']} kg CO₂
♻️Water Usage: {data['water']} liters
♻️ Sustainability Score: {data['score']}/10

♻️ Better Alternative:
{data['alternative']}"""
    
    result_show.config(text=result_text)
#Design Elements 
#Title 
title=Label(window,text="Fabric Sustainability Analyzer",font=("Times",20,"bold"))
title.pack(pady=10)
#dropown
fabric_var=StringVar()
fabric_var.set("Select a Fabric Type")

option_menu=OptionMenu(window,fabric_var,*fabrics.keys())
option_menu.pack(pady=10)
           
#BUTTON
analyse_button= Button(window,text="Analyse Button",font=("Times",12,"bold"),command=analyze_fabric)
analyse_button.pack(pady=10)
#esult
result_show=Label(window,text="",font=("Times",12,"bold"),justify=CENTER)
result_show.pack(pady=20)
window.mainloop()

              