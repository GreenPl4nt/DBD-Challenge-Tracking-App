import Save_state_manipulation as ssm

def switch_image(master,button,char_type,save,character,on_image,off_image):
    state = ssm.check_character_state(char_type=char_type,save_name=save)
    char_state = state[character]

    if char_state == 0:
        button.configure(text="", image=off_image)
        ssm.modify_character_state(char_type=char_type,save_name=save,character=character,new_state=1)
        return
    elif char_state == 1:
        button.configure(text="", image=on_image)
        ssm.modify_character_state(char_type=char_type,save_name=save,character=character,new_state=0)
        return
    