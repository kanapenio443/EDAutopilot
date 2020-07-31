def clear(to_clear=None):
    """Clears input (stop sending) any keys specified in to_clear"""
    logging.info('\n'+200*'-'+'\n'+'---- CLEAR INPUT '+183*'-'+'\n'+200*'-')
    for key in to_clear.keys():
        if key in keys:
            send(to_clear[key], state=0)
    logging.debug('clear_input')