import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import pandas as pd
import time

from sqlalchemy import create_engine

#mysql alchemy engine created to querying with MYSQL Database

engine = create_engine("mysql+mysqlconnector://root:@localhost/airbnb") 


#set up page configuration for streamlit
icon='https://avatars.githubusercontent.com/u/698437?s=280&v=4'
st.set_page_config(page_title='AIRBNB ',page_icon=icon,initial_sidebar_state='expanded',
                        layout='wide')

title_text = '''<h1 style='font-size: 36px;color:#ff5a5f;text-align: center;'>AIRBNB</h1><h2 style='font-size: 24px;color:#008891;text-align: center;'>Holiday rentals | Cabins | Beach houses</h2>'''
st.markdown(title_text, unsafe_allow_html=True)

#set up home page and option menu with side bar
with st.sidebar:


    selected = option_menu("Navigation",
                            options=["HOME","DISCOVER","INSIGHTS","POWER BI"],
                            icons=["house", "globe","lightbulb","bar-chart"],
                            default_index=0,
                            orientation="vertical",
                            styles={"container": {"width": "100%","border": "1px ridge  ","background-color": "#F84D4D","primaryColor": "#FF69B4"},
                                    "icon": {"color": "#5AFFFF", "font-size": "20px"}})
    

#set up the details for option 'Home 
if selected == "HOME":
    
    st.title("Welcome to Airbnb!")
    st.write("Find your perfect accommodation for your next adventure.")

    # Display information about Airbnb
    col1, col2 = st.columns(2)  # Adjust column widths as needed

    with col1:
        
        st.subheader(':red[Airbnb]')
        st.markdown('''Airbnb is a global online marketplace that connects travelers with unique accommodations, experiences, and hosts.
                Whether you're looking for a cozy apartment in the city, a rustic cabin in the mountains, or a beachfront villa, Airbnb offers a diverse range of stays
                to suit every traveler's needs. With Airbnb, you can discover local hospitality, immerse yourself in new cultures, and create unforgettable memories.''')

    with col2:
    
        st.image("C:/Users/dines/Downloads/AIR.jpg") 
        
    # Display history of Airbnb
    st.subheader(':red[Orgin of Airbnb]')
    st.write('''Airbnb, originally coined from “**Air Bed and Breakfast,**” is a service that lets property owners rent out their spaces to travelers looking for a place to stay.
                    Travelers can rent a space for multiple people to share, a shared space with private rooms, or the entire property for themselves.''')
    st.write('''Airbnb was founded in August 2008 by Brian Chesky, Joe Gebbia, and Nathan Blecharczyk. The idea for Airbnb came about when the founders
                rented out air mattresses in their San Francisco apartment to make extra money. Since then, Airbnb has grown into a global travel community,
                with millions of listings in over 220 countries and regions. Airbnb's mission is to create a world where anyone can belong anywhere, 
                providing unique travel experiences that promote belonging, connection, and trust.''')

    # Display pricing information
    st.subheader(':red[Monetary scheme]')
    st.write('''Airbnb is a web-based platform that connects travelers with hosts who have accommodations available for rent. Airbnb acts as an intermediary, facilitating the rental process between hosts and guests.''')
    st.image("C:/Users/dines/Downloads/Airbnb-Business-Model-Cover-Image.webp")
    st.write('''The total amount that guests pay for a stay on Airbnb includes the host's price plus Airbnb's service fee, which typically ranges from 5% to 15%.
                Hosts set their own prices for their accommodations, and Airbnb charges hosts a service fee for each booking, typically around 3%.
                Guests may also be charged additional fees, such as cleaning fees or taxes, depending on the host's settings and local regulations.''')
    
    st.write('''**For Additional info refer,**''')
    st.link_button(':red[AIRBNB WEBSITE]', url='https://www.airbnb.co.in/')

            
if selected =="POWER BI":
    st.subheader(":red[Power BI Dashboard]")
    st.image("C:/Dinesh/Project/Airbnb_project/airbnb_powerbi.png")
    st.write(":red[Note:] For Interactive dashboard, download the raw power bi file and open in Power BI")
    st.link_button('Raw Power BI File','https://github.com/DineshR03/Airbnb-analysis/blob/a8b76674e1b4675073d8881de8dbfa64684d35b8/airbnb_dashboard.pbix')
    
#set up the details for option 'Discover'
if selected == "DISCOVER":
    
    col1,col2=st.columns([2,1])

    with col2:
        st.image("C:/Users/dines/Downloads/Airbnb.gif")
        
    with col1:

        st.write(' ')
        st.subheader(':red[Discover Your Perfect Stay]')
        st.markdown('''**Explore Unique Accommodations on Airbnb! Start Your Adventure Today.**''')

        df_Country=pd.read_sql_query('''SELECT DISTINCT country from hotels_info''',con=engine)
        selected_country= st.selectbox("Search destinations",options=df_Country['country'].tolist(),index=None)
        st.write(' ')

        df_street=pd.read_sql_query('''SELECT DISTINCT street from hotels_info WHERE country =%s''',
                                    con=engine,params=[(selected_country,)])
        selected_street= st.selectbox("Select Street",options=df_street['street'].tolist(),index=None)
        st.write(' ')

        df_hotels=pd.read_sql_query('''SELECT DISTINCT name from hotels_info WHERE street =%s''',
                                    con=engine,params=[(selected_street,)])
        selected_Hotel=st.selectbox('Select Hotel',options=df_hotels['name'].tolist(),index=None)


        st.write("Selected Accommodation:", f"<span style='color:#F8CD47'>{selected_Hotel}</span>", unsafe_allow_html=True)
        

    if selected_Hotel:

            st.write(":red[Note: The information provided below is based on samples for projects.]")

                
            df=pd.read_sql_query('''SELECT name,listing_url,description,country,price,images,property_type,room_type,amenities,
                                        host_picture_url,host_name,host_url,host_about,host_location,overall_score,rating,number_of_reviews
                                        from hotels_info
                                        join rooms_info on hotels_info.id=rooms_info.id
                                        JOIN host_info on hotels_info.id = host_info.id
                                        join reviews_info on hotels_info.id = reviews_info.id
                                        where name= %s ''',con=engine,params=[(selected_Hotel,)])
                
            extract_detail = df.to_dict(orient='records')[0] 
            c1,c2=st.columns(2)
            with c1:
                    st.write('**:green[Booking Details]**')
                    st.write("**:violet[Name :]**", f'**{extract_detail['name']}**')
                    st.write("**:violet[Website Url :]**",extract_detail['listing_url'])
                    st.write("**:violet[country :]**",f'**{extract_detail['country']}**')
                    st.write("**:violet[Description :]**",extract_detail['description'])
                    st.write("**:violet[Price in $ :]**",f'**{extract_detail['price']}**')
                    st.write("**:violet[Room Type :]**",f'**{extract_detail['room_type']}**')
                    st.write("**:violet[Total Reviews :]**",f'**{extract_detail['number_of_reviews']}**')
                    st.write("**:violet[Overall Score:]**", f"**{extract_detail['overall_score']} &nbsp;&nbsp;&nbsp; **:violet[Rating:]** {extract_detail['rating']}**")


            with c2:
                    st.write('**:green[Room Details]**')
                    st.write("**:violet[Property Type :]**",f'**{extract_detail['property_type']}**')
                    st.write("**:violet[Amenities :]**",f'**{extract_detail['amenities']}**')
                    st.write('**:green[Host Details]**')
                    st.write("**:violet[Host Name :]**",f'**{extract_detail['host_name']}**')
                    st.write("**:violet[Host Url :]**",extract_detail['host_url'])
                    st.write("**:violet[Host location :]**",f'**{extract_detail['host_location']}**')
                    st.write("**:violet[Host About :]**",f'**{extract_detail['host_about']}**')
                    

            df=pd.read_sql_query('''SELECT  reviewer_name,comments FROM comments_info 
                                        join hotels_info on comments_info.id =hotels_info.id
                                        where name=%s LIMIT 10''',con=engine,params=[(selected_Hotel,)])
                
            st.write('**:green[Top Comments]**')
            st.dataframe(df,hide_index=True,use_container_width=True)
    
#set up the details for option 'Insight'
if selected == "INSIGHTS":
    select_insight=option_menu('',options=["TOP INSIGHTS","FILTER INSIGHTS"],
                                    icons=["bar-chart", "toggles"],
                                    orientation='horizontal',
                                    styles={"container":{"border":"2px ridge "},
                                    "icon": {"color": "#F8CD47", "font-size": "20px"}})
            
    if select_insight =="TOP INSIGHTS":

        opt=['Top 10 Accommodation with Highest price',
            'Top 10 Accommodation with Lowest price ',
            'Number of Hotels Count by Country',
            'Room Type Distribution by Country',
            'Top 10 Accommodation with Highest Reviews',
            'Hotels Count by Rating',
            'Average Availability of Stays by Country',
            'Average Accommodation Prices by Country',
            'Property type Distribution by country',]
        
        query=st.selectbox(':red[Select a Query]',options=opt,index=None)


        if query==opt[0]:
            col1,col2=st.columns(2)

            with col1:
                df=pd.read_sql_query('''SELECT name,country, MAX(price) as 'price' from hotels_info 
                                        GROUP by name ORDER by max(price) DESC LIMIT 10''',con=engine)
                
                fig=px.bar(df,y='name',x='price',color='name',
                        hover_data=['name','country'],title='Top 10 Accommodation with Highest price',
                        color_discrete_sequence=px.colors.qualitative.Alphabet_r)
                fig.update_layout(showlegend=False)
                st.plotly_chart(fig,use_container_width=True)
            
            with col2:
                fig=px.pie(df,names='name',values='price',color='name',
                        title='Percentage of Top 10 Accommodation with Highest price',
                        color_discrete_sequence=px.colors.cmocean.balance_r)
                fig.update_layout(showlegend=False)
                st.plotly_chart(fig,use_container_width=True)

                st.markdown('<br>', unsafe_allow_html=True)
                
            st.dataframe(df,hide_index=True,use_container_width=True)


        if query==opt[1]:
            col1,col2=st.columns(2)

            with col1:
                df=pd.read_sql_query('''SELECT name,country, min(price) as 'price' from hotels_info 
                                        GROUP by name ORDER by min(price)  LIMIT 10''',con=engine)
                
                fig=px.bar(df,y='name',x='price',color='name',
                        hover_data=['name','country'],title='Top 10 Accommodation with Lowest price',
                        color_continuous_midpoint='Viridis')
                
                fig.update_layout(showlegend=False)
                st.plotly_chart(fig,use_container_width=True)
                            
            with col2:
                fig=px.pie(df,names='name',values='price',color='name',
                        title='Percentage of Top 10 Accommodation with Lowest price',
                        color_discrete_sequence=px.colors.cmocean.balance_r)
                fig.update_layout(showlegend=False)
                st.plotly_chart(fig,use_container_width=True)

                st.markdown('<br>', unsafe_allow_html=True)
                
            st.dataframe(df,hide_index=True,use_container_width=True)



        if query==opt[2]:
            col1,col2=st.columns(2)
            
            with col1:
                df=pd.read_sql_query('''SELECT country,COUNT(name) as 'Hotel Count' FROM hotels_info GROUP BY country
                                    order by COUNT(name) Desc  ''',con=engine)

                fig=px.bar(df,x='country',y='Hotel Count',color='country',
                        hover_name='country',title="Number of Hotels Count by Country",
                        color_discrete_sequence=px.colors.qualitative.Plotly_r)
                
                fig.update_layout(showlegend=False)
                st.plotly_chart(fig,use_container_width=True)

            with col2:
                fig=px.pie(df,names='country',values='Hotel Count',color='country',
                        title="Number of Hotels by Country in percentage",
                        color_discrete_sequence=px.colors.carto.Purpor_r)
                fig.update_layout(showlegend=False)
                st.plotly_chart(fig,use_container_width=True)
                
            st.dataframe(df,hide_index=True,use_container_width=True)



        if query==opt[3]:
            
                df=pd.read_sql_query('''SELECT country,room_type,count(room_type) as 'count of room type' from rooms_info
                                    JOIN hotels_info on rooms_info.id = hotels_info.id
                                    GROUP by country, room_type''',con=engine)
                
                fig = px.sunburst(df, path=['country', 'room_type'], values='count of room type',
                        title='Room Types by Country', color_continuous_scale='RdBu')
                st.plotly_chart(fig,use_container_width=True)
                
                st.dataframe(df,hide_index=True,use_container_width=True)

                
        if query==opt[4]:
            
                df=pd.read_sql_query('''SELECT name,max(number_of_reviews) as 'Total reviews' FROM reviews_info
                                    JOIN hotels_info on reviews_info.id=hotels_info.id GROUP by hotels_info.id
                                    ORDER by MAX(number_of_reviews) DESC LIMIT 10''',con=engine)
                
                fig=px.bar(df,y='name',x='Total reviews',color='name',
                        hover_name='name',title='Top 10 Accommodation with Highest Reviews',
                        color_discrete_sequence=px.colors.qualitative.Bold_r)
                
                fig.update_layout(showlegend=False)
                st.plotly_chart(fig,use_container_width=True)

                st.dataframe(df,hide_index=True,use_container_width=True)


        if query==opt[5]:
                
                df=pd.read_sql_query('''SELECT  rating ,count(id) as 'total stays'from reviews_info
                                GROUP by rating order by rating desc ''',con=engine)
                
                fig=px.line(df,x='rating',y='total stays',markers=True,
                        title='Hotels Count by Rating')
                
                fig.update_layout(showlegend=False)
                st.plotly_chart(fig,use_container_width=True)

                st.dataframe(df,hide_index=True,use_container_width=True)
                

        if query==opt[6]:
                
                df=pd.read_sql_query('''SELECT country,AVG(availability_30) as 'avg_availability_30',AVG(availability_60)  as 'avg_availability_60',
                                    AVG(availability_365) as 'avg_availability_365' from rooms_info
                                    join hotels_info on rooms_info.id=hotels_info.id GROUP by country ''',con=engine)
                
                fig = px.bar(df, x='country', y=['avg_availability_30', 'avg_availability_60', 'avg_availability_365'],
                            title='Average Availability of Stays by Country',
                            labels={'value': 'Average Availability', 'variable': 'Availability Period', 'country': 'Country'},
                            barmode='group')

                st.plotly_chart(fig,use_container_width=True)
                
                st.dataframe(df,hide_index=True,use_container_width=True)


        if query==opt[7]:
                
                df=pd.read_sql_query('''SELECT country ,AVG(price) as 'Average Price' from hotels_info 
                                    group by country order by AVG(price) desc ''',con=engine)

                fig=px.bar(df,x='country',y='Average Price',color='country',
                        hover_name='country',title='Average Accommodation Prices by Country')

                st.plotly_chart(fig,use_container_width=True)

                               
                st.dataframe(df,hide_index=True,use_container_width=True)


        if query==opt[8]:
            
                df=pd.read_sql_query('''SELECT country,property_type,count(room_type) as 'Property Count' from rooms_info
                                    JOIN hotels_info on rooms_info.id = hotels_info.id
                                    GROUP by country,property_type''',con=engine)
                
                fig = px.sunburst(df, path=['country','property_type'], values='Property Count',
                        title='Property type Distribution by country', color_continuous_scale='RdBu')
                st.plotly_chart(fig,use_container_width=True)
                
                st.dataframe(df,hide_index=True,use_container_width=True)

    if select_insight =="FILTER INSIGHTS":

        Ques=['Property wise Accommodation count and Average price for specific country',
                'Room type wise Accommodation count and Average price for specific country',
                'Average Availability days for specific property and country',
                'Country wise Average price of stays for specific Property and Room type',
                'Average pricing and fees for a speciific country',
                'Cancellation Policy-wise Stays Count for a Specific Country',]
        
        query=st.selectbox(':red[Select a Query]',options=Ques,index=None)

        if query==Ques[0]:

            st.markdown('<br>', unsafe_allow_html=True)
            df_Country=pd.read_sql_query('''SELECT DISTINCT country from hotels_info''',con=engine)
            selected_country= st.selectbox("Select a country",options=df_Country['country'].tolist(),index=None)

            if selected_country:

                df=pd.read_sql_query('''SELECT property_type,avg(price)  as 'Average price',COUNT(property_type) as 'Total Stays' from rooms_info 
                                        join hotels_info on rooms_info.id=hotels_info.id   where country= %s
                                        GROUP by property_type''',con=engine,params=[(selected_country,)])
                
                fig=px.scatter(df,x='property_type',y='Total Stays',color='property_type',
                        labels={'property_type': 'Property Type', 'Total Stays': 'Total Stays'},
                        title=f'Property wise Accommodation count for {selected_country}')
                
                st.plotly_chart(fig,use_container_width=True)

                col1,col2=st.columns(2)
                with col1:
                    fig=px.pie(df,names='property_type',values='Average price',color='property_type',
                            title=f'Property wise Average price for {selected_country}',
                            color_discrete_sequence=px.colors.qualitative.Safe)
                    
                    fig.update_layout(showlegend=False)
                    st.plotly_chart(fig,use_container_width=True)

                with col2:
                    st.write('**Dataframe**')
                    st.dataframe(df,hide_index=True,use_container_width=True)


        if query==Ques[1]:

            st.markdown('<br>', unsafe_allow_html=True)
            df_Country=pd.read_sql_query('''SELECT DISTINCT country from hotels_info''',con=engine)
            selected_country= st.selectbox("Select a country",options=df_Country['country'].tolist(),index=None)

            if selected_country:

                df=pd.read_sql_query('''SELECT room_type,avg(price)  as 'Average price',COUNT(room_type) as 'Total Stays' from rooms_info 
                                        join hotels_info on rooms_info.id=hotels_info.id   where country= %s
                                        GROUP by room_type''',con=engine,params=[(selected_country,)])
                
                fig=px.bar(df,x='room_type',y='Total Stays',color='room_type',
                        labels={'room_type': 'Room Type', 'Total Stays': 'Total Stays'},
                        title=f'Room Type wise Accommodation count for {selected_country}',barmode='group')
                
                st.plotly_chart(fig,use_container_width=True)

                col1,col2=st.columns(2)
                with col1:
                    fig=px.pie(df,names='room_type',values='Average price',color='room_type',
                            title=f'Room Type wise Average price for {selected_country}',
                            color_discrete_sequence=px.colors.qualitative.Safe)
                    
                    fig.update_layout(showlegend=False)
                    st.plotly_chart(fig,use_container_width=True)

                with col2:
                    st.write('**Dataframe**')
                    st.dataframe(df,hide_index=True,use_container_width=True)
            
        if query==Ques[2]:

            st.markdown('<br>', unsafe_allow_html=True)

            df_Country=pd.read_sql_query('''SELECT DISTINCT country from hotels_info''',con=engine)
            selected_country= st.selectbox("Select a country",options=df_Country['country'].tolist(),index=None)

            df_property=pd.read_sql_query('''SELECT DISTINCT property_type from rooms_info 
                                        join hotels_info on rooms_info.id = hotels_info.id where country=%s''',engine,params=[(selected_country,)])
            selected_prop=st.selectbox('select a property',options=df_property['property_type'].tolist(),index=None)

            if selected_prop:

                df=pd.read_sql_query('''SELECT country,AVG(availability_30) as 'avg_availability_30',AVG(availability_60)  as 'avg_availability_60',
                                        AVG(availability_365) as 'avg_availability_365' from rooms_info
                                        join hotels_info on rooms_info.id=hotels_info.id 
                                        where country =%s AND property_type=%s ''',con=engine,params=[(selected_country,selected_prop)])
                    
                fig = px.bar(df, x='country', y=['avg_availability_30', 'avg_availability_60', 'avg_availability_365'],
                                title=f'Average Availability days for {selected_prop} in {selected_country}',
                                labels={'value': 'Average Availability', 'variable': 'Period'},
                                barmode='group')
                st.plotly_chart(fig,use_container_width=True)

                st.write('**Dataframe**')
                st.dataframe(df,hide_index=True,use_container_width=True)

        if query==Ques[3]:
            st.markdown('<br>', unsafe_allow_html=True)

            df_property=pd.read_sql_query('''SELECT DISTINCT property_type from rooms_info ''',con=engine)
            selected_prop=st.selectbox('select a property',options=df_property['property_type'].tolist(),index=None)

            df_room=pd.read_sql_query('''SELECT DISTINCT room_type from rooms_info 
                                        where property_type=%s ''',engine,params=[(selected_prop,)])
            selected_room=st.radio('select a Room type',options=df_room['room_type'].tolist(),index=None)

            if selected_room:

                df=pd.read_sql_query('''SELECT country, AVG(price) as 'average price' FROM hotels_info 
                                        JOIN rooms_info ON hotels_info.id = rooms_info.id 
                                        WHERE rooms_info.property_type =%s and rooms_info.room_type=%s
                                        GROUP BY country;''',con=engine,params=[(selected_prop,selected_room)])
                
                fig = px.bar(df, x='country', y='average price',color='country',
                                title=f'country wise Average price of stay for {selected_prop} and {selected_room}',
                                labels={'country': 'country', 'average price': 'average price'},
                                color_discrete_sequence=px.colors.qualitative.Bold_r)
                
                st.plotly_chart(fig,use_container_width=True)
                st.dataframe(df,hide_index=True,use_container_width=True)

        if query==Ques[4]:
                st.markdown('<br>', unsafe_allow_html=True)
                
                df_Country=pd.read_sql_query('''SELECT DISTINCT country from hotels_info''',con=engine)
                selected_country= st.selectbox("Select a country",options=df_Country['country'].tolist(),index=None)

                if selected_country:
                    chek=st.checkbox(f"Click to view pricing details by property type in {selected_country}.")

                    if not chek:

                        df=pd.read_sql_query('''SELECT country,AVG(weekly_price) as 'avg Weekly price',AVG(monthly_price)  as 'avg Monthly price',
                                            AVG(security_deposit) as 'avg security deposit', AVG(cleaning_fee) as 'avg cleaning price'
                                            from hotels_info  where country=%s GROUP by country ''',con=engine,params=[(selected_country,)])
                        
                        fig = px.bar(df, x='country', y=['avg Weekly price', 'avg Monthly price', 'avg security deposit','avg cleaning price'],
                                    title=f'Average Pricing and Fees of stays in {selected_country} ',
                                    labels={'value':'Average pricing', 'variable':'cataogory' },
                                    barmode='group')
                        
                        st.plotly_chart(fig,use_container_width=True)

                    if chek:

                        df_property=pd.read_sql_query('''SELECT DISTINCT property_type from rooms_info 
                                        join hotels_info on rooms_info.id = hotels_info.id where country=%s''',engine,params=[(selected_country,)])
                        selected_prop=st.selectbox('select a property',options=df_property['property_type'].tolist(),index=None)

                        if selected_prop:

                            df=pd.read_sql_query('''SELECT country,AVG(weekly_price) as 'avg Weekly price',AVG(monthly_price)  as 'avg Monthly price',
                                                    AVG(security_deposit) as 'avg security deposit', AVG(cleaning_fee) as 'avg cleaning price'
                                                    from hotels_info  join rooms_info on hotels_info.id=rooms_info.id
                                                    where country=%s and property_type=%s GROUP by country''',con=engine,params=[(selected_country,selected_prop)])
                            
                            fig = px.bar(df, x='country', y=['avg Weekly price', 'avg Monthly price', 'avg security deposit', 'avg cleaning price'], 
                                        title=f'Average Price & Fees in {selected_country} - property type : {selected_prop}',
                                        labels={'value':'Average pricing', 'variable':'cataogory' },
                                        color_discrete_sequence=px.colors.qualitative.D3_r,
                                        barmode='group')
                            
                            st.plotly_chart(fig,use_container_width=True)

        if query==Ques[5]:
            st.markdown('<br>', unsafe_allow_html=True)
                
            df_Country=pd.read_sql_query('''SELECT DISTINCT country from hotels_info''',con=engine)
            selected_country= st.selectbox("Select a country",options=df_Country['country'].tolist(),index=None)

            if selected_country:
                    chek=st.checkbox(f"Click to view property wise count of stays for {selected_country} ")

                    if not chek:

                        df=pd.read_sql_query('''SELECT cancellation_policy, COUNT(*) AS 'Stays Count' FROM hotels_info
                                JOIN rooms_info ON hotels_info.id = rooms_info.id
                                WHERE country = %s GROUP BY cancellation_policy''',con=engine,params=[(selected_country,)])
                        
                        fig = px.bar(df, x='cancellation_policy', y='Stays Count', color='cancellation_policy',
                                    title=f'Cancellation Policy-wise Stays Count for {selected_country}',
                                    labels={'cancellation_policy': 'Cancellation Policy', 'Stays Count': 'Stays Count'})
                        
                        st.plotly_chart(fig,use_container_width=True)

                    if chek:

                        df_property=pd.read_sql_query('''SELECT DISTINCT property_type from rooms_info 
                                        join hotels_info on rooms_info.id = hotels_info.id where country=%s''',engine,params=[(selected_country,)])
                        selected_prop=st.selectbox('select a property',options=df_property['property_type'].tolist(),index=None)

                        if selected_prop:

                            df=pd.read_sql_query('''SELECT country, cancellation_policy, COUNT(*) AS 'Stays Count' FROM hotels_info
                                JOIN rooms_info ON hotels_info.id = rooms_info.id
                                WHERE country =%s and  property_type=%s
                                GROUP BY country, cancellation_policy''',con=engine,params=[(selected_country,selected_prop)])
                            
                            fig = px.pie(df, values='Stays Count', names='cancellation_policy',hole=0.3,
                                    title=f'Cancellation Policy-wise Stays Count for {selected_prop} in {selected_country}',
                                    labels={'Stays Count': 'Stays Count', 'cancellation_policy': 'Cancellation Policy'})
                            
                            st.plotly_chart(fig,use_container_width=True)


