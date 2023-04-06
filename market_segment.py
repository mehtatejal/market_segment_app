import streamlit as st
import pandas as pd
import pickle
import urllib.request

# Set the title of the app
st.title("Market Segmentation App")

from PIL import Image
st.subheader("Hello!    Welcome to Product Recommendation")
# st.set_page_config(page_title = 'Welcome to Product Recommendation', layout='centered')
# st.title("Customer Segment App")
image = Image.open("MarketSegment.png")
st.image(image,use_column_width = True)

text = "<b>This app is designed to help businesses decide which product they should focus on to sell more. The app recommends which product out of the 13 categories of products named Columbian, Lemon, Decaf Espresso, Darjeeling, Chamomile, Early Grey, Caffe Mocha, Decaf Irish Cream, Caffe Latte, Regular Espresso, Mint, Amaretto and Green Tea will be most likely to sell based on certain factors. These factors include the State, Market, Market Size, Product Type, and Type. The app's prediction accuracy is approximately 75%, making it a reliable tool for businesses to plan their inventory, make decisions regarding offers, and determine the price of the product. By entering the relevant details, businesses can receive data-driven suggestions that will help them increase their sales and profitability.</b>"
st.write(text, unsafe_allow_html=True)

#load the model
# classifier = pickle.load(open('final_pipeline.pkl','rb'))
url = "https://github.com/mehtatejal/market_segment_app/raw/main/final_pipeline.pkl"
with urllib.request.urlopen(url) as f:
    classifier = pickle.load(f)


# customer segmentation function
def segment_customers(input_data):
    data = pd.DataFrame(input_data, columns=['State', 'Market', 'Market Size', 'Product Type', 'Type'])
    prediction=classifier.predict(data)
#     prediction=classifier.predict(pd.DataFrame(input_data, columns=['State', 'Market', 'Market Size', 'Product Type', 'Type']))
    output_str = prediction[0]
    return ("In "+data['State']+", "+output_str+" has the best potential to succeed in" +data['Market Size']+"market for product type "+data['Product Type'] )

def main():
    
    state_names = ['Connecticut','Washington','California','Texas','New York','Ohio','Illinois','Louisiana','Florida','Wisconsin','Colorado','Missouri','Iowa',
    'Massachusetts','Oklahoma','Utah','Oregon','New Mexico','New Hampshire','Nevada'] 
    State = st.selectbox("Select a state:", state_names)
#     State = st.text_input("Type In The State",type='default')
    Market = st.radio ( "Select Market", ('East', 'West','South','Central'))
    Market_Size = st.radio ( "Select Market Size", ('Small Market', 'Major Market'))
    Product_Type = st.radio ( "Select Product Type", ("Coffee","Tea","Espresso","Herbal Tea"))
    Type = st.radio ( "Please Select The Type", ('Regular', 'Decaf') )
    
    
    result = ""

    # when button is clicked, make the prediction and store it
    if st.button("Recommend Product"):
        # Check if the name field is empty
        if not State:
           st.warning("Please enter State Name")
        else:
           result=segment_customers([[State,Market,Market_Size,Product_Type,Type]])
    
    st.success(result)
    

if __name__ == '__main__':
        main ()


