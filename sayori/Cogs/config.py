import json


class conf():

    config = json.loads(open("../config.json", "r").read())
    token = config["sayori_token"]
    prefix1 = "t_"
    prefix2 = "T_"
    name = "Sayori"
    cogd = "Cogs"
    type_speed = 2
    playing_msg = ["Type 's_help' for help!","Doki Doki Literature Club","with the crayons!","Katawa Shoujo","with Mr. Cow!","with a noose!"]
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
    norm = 0x3eb0ff # The Normal Embed Color
    warn = 0xff42e2 # The Warning Embed Color
    suc = 0xff42e2 # The Success Embed Color

    # Response for if someone tries to ping everyone upon bot interaction.
    everyone_tag = "We don't need to get everyone's attention!"

    # TODO: Move this to database.
    # This array will be filled with guild IDs on startup, with indexes that can be removed by disabling chat triggers or shutting down the bot.
    w_tog_on = []

    ''' Doki Bot's IDs '''
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

