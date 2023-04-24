import streamlit as st

def option_return(option_type:str, buy_sell:str, lot_size:int, premium:float, strike_price:float, final_price:float):
    lot_size = lot_size*100
    if buy_sell == 'sell':
        if option_type == 'call':
            if final_price < strike_price:
                opt_return = premium * lot_size
            else:
                opt_return = (strike_price - final_price) * lot_size + premium * lot_size

        elif option_type == 'put':
            if final_price > strike_price:
                opt_return = premium * lot_size
            else:
                opt_return = (final_price - strike_price) * lot_size + premium * lot_size

    elif buy_sell == 'buy':
        if option_type == 'call':
            if final_price < strike_price:
                opt_return = - premium * lot_size
            else:
                opt_return = (final_price - strike_price) * lot_size- premium * lot_size

        elif option_type == 'put':
            if final_price > strike_price:
                opt_return = - premium * lot_size
            else:
                opt_return = (strike_price - final_price) * lot_size- premium * lot_size

    return opt_return



option_types = []
buy_sells = []
lot_sizes = []
premiums = []
strike_prices = []
final_prices = []
st.write("Please assume price on maturity")
final_prices.append(st.number_input('Final Price', key='final_price_0'))
st.write("Option 1")
col1, col2, col3= st.columns(3)
with col1:
    option_types.append(st.selectbox('Option Type', ['call', 'put'], key='option_type_0'))
    buy_sells.append(st.selectbox('Buy/Sell', ['buy', 'sell'], key='buy_sell_0'))

with col2:
    lot_sizes.append(st.number_input('Lot Size', key='lot_size_0'))
    premiums.append(st.number_input('Premium', key='premium_0'))
with col3:
    strike_prices.append(st.number_input('Strike Price', key='strike_price_0'))
    
result1 = option_return(option_types[0], buy_sells[0], lot_sizes[0], premiums[0], strike_prices[0], final_prices[0])
st.write(f'P&L value is {result1}')

st.write("Option 2")
col1, col2, col3= st.columns(3)
with col1:
    option_types.append(st.selectbox('Option Type', ['call', 'put'], key='option_type_1'))
    buy_sells.append(st.selectbox('Buy/Sell', ['buy', 'sell'], key='buy_sell_1'))
with col2:
    lot_sizes.append(st.number_input('Lot Size', key='lot_size_1'))
    premiums.append(st.number_input('Premium', key='premium_1'))
with col3:
    strike_prices.append(st.number_input('Strike Price', key='strike_price_1'))

result2 = option_return(option_types[1], buy_sells[1], lot_sizes[1], premiums[1], strike_prices[1], final_prices[0])
st.write(f'P&L value is {result2}')

st.write("Option 3")
col1, col2, col3= st.columns(3)
with col1:
    option_types.append(st.selectbox('Option Type', ['call', 'put'], key='option_type_2'))
    buy_sells.append(st.selectbox('Buy/Sell', ['buy', 'sell'], key='buy_sell_2'))
with col2:
    lot_sizes.append(st.number_input('Lot Size', key='lot_size_2'))
    premiums.append(st.number_input('Premium', key='premium_2'))
with col3:
    strike_prices.append(st.number_input('Strike Price', key='strike_price_2'))
 
result3 = option_return(option_types[2], buy_sells[2], lot_sizes[2], premiums[2], strike_prices[2], final_prices[0])
st.write(f'P&L value is {result3}')

if st.button('Calculate'):
    result = 0
    for i in range(len(option_types)):
        result += option_return(option_types[i], buy_sells[i], lot_sizes[i], premiums[i], strike_prices[i], final_prices[0])
    
    st.write(f'Total P&L value is {result}')