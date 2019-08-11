import json


class conf():

    config = json.loads(open("../config.json", "r").read())
    prefix1 = "mc_"
    prefix2 = "Mc_"
    name = "MC"
    type_speed = 2
    playing_msg = [f"Type 'mc_help' for help!","Doki Doki Literature Club","with a shoe lace","aloof","in a dark void"]
    admins = [480580173431832577, 310496481435975693, 270057011251642368, 320286336433258506]
    #         Tsumiki             IDroid              Cole                Illuminati
    test_mode = config["test_mode"]  # To enable this function, change this to True in config.json

    if "false" in test_mode.lower():
        sharding = True
        version = "4.0L Dragonfruit"
    else:
        sharding = False
        version = "4.0B Dragonfruit" # Testing mode should be beta.
    #L|Launch    B|Beta

    # These hex codes are for embed colors. The "norm" hex is different for each doki and MC.
    err = 0xC91313 # The Error Embed Color
    norm = 0xdb7915 # The Normal Embed Color
    warn = 0xff42e2 # The Warning Embed Color
    suc = 0xff42e2 # The Success Embed Color

    # TODO: Move this to database.
    # This array will be filled with guild IDs of those that disable chat triggers. The array is cleared on shutdown.
    w_tog_off = []

    ''' Doki Bot's IDs'''
    if not "false" in test_mode.lower():
        natsuki_id = 531555963908653076
        monika_id = 531556928732528670 
        sayori_id = 531554745337249792
        yuri_id = 531556397746356224
        mc_id = 596409849131171870

    else:
        natsuki_id = 433834936450023424
        monika_id = 436351740787294208 
        sayori_id = 425696108455657472
        yuri_id = 436350586670153730
        mc_id = 596407346176065552

