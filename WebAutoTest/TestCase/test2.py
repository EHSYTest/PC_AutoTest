def get_so_by_url():
    order_id = ''
    while not order_id.startswith('SO'):
        url = 'SO150330024737557715'
        order_id = url[-20:]
        print(order_id)
    return order_id


order = get_so_by_url()