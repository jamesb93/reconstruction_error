def max_post(console_post, client_obj):
    '''
    A wrapper for sending messages back to Max in the console. Makes for easy debugging and GUI.
    '''
    client_obj.send_message('/post', console_post)
