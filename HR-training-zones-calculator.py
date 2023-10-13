import streamlit as st

st.set_page_config(
    page_title="Heart rate training zones calculator",
    page_icon="media/favicon.ico",
    layout="centered",
    initial_sidebar_state="auto",
    #menu_items={
        #'Get Help': '<<URL>>',
        #'Report a bug': "<<URL>>",
        #'About': "Made with Streamlit v1.27.0"
    #}
)

# html strings used to render donate button and link and text
donate_text = '<h6> Useful? Buy us a coffee. </h6>'

html_donate_button = '''
<form action="https://www.paypal.com/donate" method="post" target="_blank">
<input type="hidden" name="hosted_button_id" value="6X8E9CL75SRC2" />
<input type="image" src="https://www.paypalobjects.com/en_GB/i/btn/btn_donate_SM.gif" border="0" name="submit" title="PayPal - The safer, easier way to pay online!" alt="Donate with PayPal button"/>
<img alt="" border="0" src="https://www.paypal.com/en_GB/i/scr/pixel.gif" width="1" height="1" />
</form>
'''   

def redirect_button(url: str):
    st.markdown(
    f"""
    <a href="{url}" target="_blank">
        <div>
        <img src="https://www.paypalobjects.com/en_GB/i/btn/btn_donate_SM.gif" alt="Donate with PayPal button">
        </div>
    </a>
    """,
    unsafe_allow_html=True
    )

st.image('media/logo.png', width=100)
st.title('Heart rate training zones calculator')

st.write('This app helps you develop training schedules to achieve your fitness goals by calculating your heart rate training zones. To get started, just enter your age below. If you need an explanation, expand the Notes section below.')


age = st.number_input('What\'s your age?', min_value=0, max_value=110, step=1, value=None)

if age:
    mhr1 = 220 - age
    mhr2 = 208 - (0.7 * age)
    mhr3 = 211 - (0.64 * age)
    hr_calcs = [mhr1, mhr2, mhr3]
    calc_max_hr = int(max(hr_calcs))
    
    st.write('\n')
    st.write('Based on your age, this is your calculated maximum heart rate in beats per minute (bpm). However you can overide the calculated value if you want.')
    max_heart_rate = st.slider('Maximum heart rate (bpm)', min_value=100, max_value=250, step=1, value=calc_max_hr)
    zone1 = (0.65 * max_heart_rate)
    zone2 = (0.8 * max_heart_rate)
    zone3 = (0.88 * max_heart_rate)
    zone4 = (0.92 * max_heart_rate)
    zonei = (0.98 * max_heart_rate)

    st.write('\n')
    st.divider()
    zone1_string = '<strong><em>Your easy training zone is <span style="color:#F63366;"> ' + "%.0f" % zone1 + ' to ' + "%.0f" % zone2 + ' bpm</span></em></strong>. Beginners should spend all their time in this zone for a few weeks at least. Experienced distance athletes should spend over half their time in this zone using it for your warm ups, cool downs, recovery periods between fast repetitions and the long Sunday run/ride. Develops most of the systems needed for endurance events.'
    st.markdown(zone1_string, unsafe_allow_html=True)
    st.divider()
    zone2_string = '<strong><em>Your comfortable training zone is <span style="color:#F63366;"> ' + "%.0f" % zone2 + ' to ' + "%.0f" % zone3 + ' bpm</span></em></strong>. Experienced distance athletes can maintain this intensity for several hours so it\'s your marathon running or sportive intensity. In terms of training stress, it\'s about twice as hard as your easy training zone so do about 25% of your training in this zone.'
    st.markdown(zone2_string, unsafe_allow_html=True)
    st.divider()
    zone3_string = '<strong><em>Your threshold training zone is <span style="color:#F63366;"> ' + "%.0f" % zone3 + ' to ' + "%.0f" % zone4 + ' bpm</span></em></strong>. Lactate threshold intensity. Improves speed endurance (your ability to hang on to a hard pace). Aim for about 10\% of your weekly mileage or up to an hour a week at this intensity.'
    st.markdown(zone3_string, unsafe_allow_html=True)
    st.divider()
    zone4_string = '<strong><em>Your interval training zone is <span style="color:#F63366;"> ' + "%.0f" % zone4 + ' to ' + "%.0f" % max_heart_rate + ' bpm</span></em></strong>. Speed work to improve your VO\u2082max. Repeated work intervals of up to 5 minutes each with easy zone recoveries of similar duration. Hard physically and mentally so aim for no more than 8% of your weekly mileage in this zone. Or if you are happy with the pace you run or ride at already and just want to go further, skip them completely.'
    st.markdown(zone4_string, unsafe_allow_html=True)
    st.divider()
    zonei_string = '<strong><em>Your repetition training zone is <span style="color:#F63366;"> ' + "%.0f" % zonei + ' to ' + "%.0f" % max_heart_rate + ' bpm</span></em></strong>. Speed work to develop running economy and power. Repeated work efforts of up to 2 minutes each at an intensity you could only keep up for about 5 or 10 minutes maximum with full recoveries in between. Up to about 5% of your weekly mileage. Your heart rate is likely to hit the buffers towards the end of the repetitions so this is only for experienced exercisers.'
    st.markdown(zonei_string, unsafe_allow_html=True)
    st.divider()




st.write('\n')
st.write('\n')
donate_left, donate_right = st.columns([1, 3])
with donate_left:
    st.write('\n')
    st.markdown(donate_text, unsafe_allow_html=True)

with donate_right:
    st.write('\n')
    redirect_button("https://www.paypal.com/donate/?hosted_button_id=6X8E9CL75SRC2")   

st.write('\n')
st.write('\n')
notes = st.button('Notes')

notes_container1 = st.empty()
if notes:
    notes_string = 'Heart rate training works because your pace will vary with hills and headwinds and so on but as long as your heart rate stays the same, the intensity of the effort and training effect will be broadly the same regardless. Heart rate training zones are calculated as a percentage of your maximum heart rate. A common estimate of this for runners is *(220 minus your age)*. However many older athletes find this gives too low a value for them so a couple of other formulas are commonly used *(208 - [0.7 * your age] and 211 - [0.64 * your age])*. This app takes the maximum of all three methods as your calculated maximum heart rate. (Some methods also take your resting heart rate into account but it has to be measured under such controlled conditions to be reliable that we choose to keep it simple here.) If you are new to exercise, go with the calculated value; it\'ll be close enough for your training purposes and you aren\'t in danger of dropping dead from a heart attack trying to find out your true value. However you can override the calculated value using the slider if you know your own maximum heart rate already. If you don\'t know your maximum heart rate, the highest value you see on the clock at the end of a 20 minute race or at failure in a beep test are good ways of finding out. Or go flat out at your chosen exercise for 2 minutes, rest a minute and repeat until you just can\'t keep the efforts up any more. The highest heart rate you see before tailing off will be at or near your maximum. It\'s tough but it\'s worth doing if your sport is something other than running; cycling maximum heart rates are often lower than running MHRs for the same individual.<br><br>The heart rate zones here are based on the methods of legendary running coach and exercise physiologist [Jack Daniels](https://en.wikipedia.org/wiki/Jack_Daniels_(coach)). They differ from the more common Karvonen method zones by having a much narrower zone 3 (the threshold training zone in Jack\'s nomenclature). Threshold is the point at which your body can\'t supply enough oxygen any more and you start to go deeply anaerobic and rapidly build up lactate in your blood. From this it follows that zones 1 and 2 (your easy and comfortable training zones) are almost entirely aerobic. This is where you teach your body to burn fat as a fuel so you can go long without hitting the wall or bonking on your bike. The easy zone gets you most of the benefits of endurance training: it\'s intense enough to bring a training effect without stressing your body so hard you can\'t get out the next day. The comfortable training zone is about the intensity you\'d race at in an event lasting several hours (i.e. it\'s marathon running or sportive cycling pace). It gets you used to judging that pace, feeding on the move and can be used to break up a bit of the tedium of plodding along at easy pace. The one thing you won\'t get from training exclusively in these zones is much faster: you\'ll tend to go longer, more comfortably but if you want to go faster you\'ll want to start putting some anaerobic work into your schedule. The threshold zone is the point at which your body is beginning to struggle to flow oxygen to your muscles fast enough. Training in this zone builds your speed endurance: your ability to hang on to a pace. If you only have time for a couple of 20 minute cardio training sessions a week, doing them at threshold intensity will probably get you the most return for your time. For athletes with bigger training schedules, aim for about 10% of your training time in this zone. You are burning glycogen almost exclusively at this intensity and because your body doesn\'t have much of it, most people can\'t keep this intensity up for more than an hour (for runners it roughly corresponds to your 10k race pace and for good cyclists your 25 mile time trail pace). Try either doing your threshold work as one long session or do it as, say, 15 minute bursts interspersed with easy zone work: mix it up, keep it interesting. The interval and repetition zones are more deeply anaerobic; it\'s where you are overstressing the ability of your heart, lungs, vascular system and mitochondria to supply oxygen to your muscles. You are burning entirely glycogen at these intensities and doing it increasingly inefficiently resulting in lactate build up in your blood which is what makes training at these intensities so hard. Training in these zones should make you faster, stronger and improve your VO\u2082max (maximum rate at which you can flow oxygen to your muscles). But it won\'t do much to improve your chance of completing a marathon or to get around a sportive because you don\'t have enough glycogen to cover these distances, and that\'s the only fuel you are using in zones 4 and 5. It\'s also tough mentally and physically which is why the 8% and 5% of your weekly mileage recommendations are there. The other difficulty of training in these zones is getting the pacing right; because your heart rate is only getting to target towards the end of the work interval, there\'s a tendency to go too hard in the early work sessions, finding yourself unable to maintain pace in the later ones. As a guide, your interval training pace is about the pace you could maintain for a 20 minute race (so about 5k pace for good runners or 10 mile TT pace for good cyclists) and your repetition pace is a pace you could maintain for a few minutes (so about 1 mile race pace for runners).<br><br>Finally, if running is your sport and you are doing it primarily for weight loss, a few observations. (It varies a bit depending on your size but) generally no matter how fast you run, you\'re burning about 100 calories a mile. This is about the number of calories in one biscuit. There are about 3700kcal in 1lb (0.45kg) of adipose tissue (\'body fat\'). From this you can work out that you need to run a lot of miles to lose much weight unless you accompany it with diet and lifestyle changes. Men\'s Health style articles will often tell you that high intensity interval training burns more calories and raises your metabolism more than plodding along at easy pace so is better for weight loss. There\'s some truth in this and it\'s seductive because everyone likes the idea of more for less. But hand in hand with that is the fact that because the efforts are so hard you can manage fewer of them per session interspersed with relatively long rest periods. When you work it all out, no matter what style of running training you do, most people are using between about 600 and 800 calories an hour. (For cyclists it\'s harder to generalise about because for them aerodynamic drag dominates so their energy use goes up exponentially with speed.) Don\'t expect to lose much weight if you do two 20 minute running sessions a week and wash them down with a Big Mac.<br><small>*Comments, queries or suggestions? [Contact us](https://www.elephant-stone.com/contact.html)*.</small>'
    notes_container1.markdown(notes_string, unsafe_allow_html=True)
    hide =st.button('Hide notes')
    if hide:
        notes = not notes
        notes_container1 = st.empty()    

