from sources import IdentifyLink
import sys
import webbrowser

def usage_alert():
    print('Usage: link_identifier.py -option link/query')

def help_():
    usage_alert()
    webbrowser.open('README.md')

def link_alert():
    print('Link must be a valid youtube link')

def details_alert():
    print('This link is a rickroll!')

def not_found_alert():
    print("This link doesn't seem like a rickroll yet. It is suggested you analyse the other parameters as well.")

def analyse_link(link_provided):
    if 'https' not in link_to_identify or ':' not in link_to_identify or '/' not in link_to_identify:
        link_alert()
        exit()

if __name__ == '__main__':
    arg_list = sys.argv
    if len(arg_list) < 2:
        usage_alert()
        exit(1)

    else:
        if arg_list[1] == '-h':
            help_()

        elif arg_list[1] == '-u':
            usage_alert()

        elif arg_list[1] == '-t' or arg_list[1] == '-c' or arg_list[1] == '-pl' or arg_list[1] == '-d' or arg_list[1] == '-od' or arg_list[1] == '-cmt' or arg_list[1] == '-dsc' or arg_list[1] == '-plv' or arg_list[1] == '-chnc':
            try:
                link_to_identify = arg_list[2]

            except IndexError as E:
                usage_alert()
                exit()

            analyse_link(link_to_identify)

            try:
                tc_target = IdentifyLink(link_to_identify)

            except TypeError:
                link_alert()
                exit()

            if arg_list[1] == '-t':
                parameter_ =  tc_target.get_link_details()[0].upper()

                if 'RICKROLL' in parameter_ or 'RICK ROLL' in parameter_ or 'RICK-ROLL' in parameter_ or 'RICK ASTLEY' in parameter_:
                    details_alert()

                else:
                    not_found_alert()

                tc_target.close_driver()

            elif arg_list[1] == '-c':
                copyright_ = tc_target.copyright()

                if copyright_ == 'Rick Astley - Never Gonna Give You Up (Video)':
                    details_alert()

                else:
                    not_found_alert()

                tc_target.close_driver()

            elif arg_list[1] == '-pl':
                if tc_target.playlist_name()[1] == None:
                    print('No playlist found')

                else:
                    playlist_name = tc_target.playlist_name()[1].upper()
                    if 'RICK ASTLEY' in playlist_name or 'RICK-ROLL' in playlist_name or 'RICK ROLL' in playlist_name:
                        details_alert()

                    else:
                        not_found_alert()

                tc_target.close_driver()

            elif arg_list[1] == '-d':
                list_ = tc_target.get_link_details()
                list_.insert(0, "Title:")
                list_.insert(2, "Views:")
                list_.insert(4, "Date:")
                list_.insert(6, "Likes:")
                list_.insert(8, "Dislikes: ")
                print(list_)
                tc_target.close_driver()

            elif arg_list[1] == '-od':
                list_ = tc_target.other_details()
                list_.insert(0, "Channel name:")
                list_.insert(2, "Subscriber count:")

                print(list_)
                tc_target.close_driver()

            elif arg_list[1] == '-cmt':
                comments_ = tc_target.comments()

                if comments_ == None:
                    not_found_alert()

                for comments in comments_:
                    if 'RICK ROLL' in comments.upper() or 'RICKROLL' in comments.upper() or 'RICK ASTLEY' in comments.upper():
                        details_alert()
                        break

                    else:
                        not_found_alert()
                        print('You can take a look at some of the comments:')
                        print(comments_[0:15])
                        break

                tc_target.close_driver()

            elif arg_list[1] == '-dsc':
                print(tc_target.total_description())
                tc_target.close_driver()

            elif arg_list[1] == '-plv':
                if tc_target.playlist_name()[1] == None:
                    print('No playlist found')

                else:
                    print(tc_target.playlist_name()[0])

                tc_target.close_driver()

            elif arg_list[1] == '-chnc':
                channel_name = tc_target.other_details()[0]

                if channel_name == 'Bajà Blast' or channel_name == 'Official Rick Astley' or 'RICK ROLL' in channel_name.upper() or 'RICK-ROLL' in channel_name.upper() or 'RICK ASTLEY' in channel_name.upper():
                    details_alert()

                else:
                    not_found_alert()

                tc_target.close_driver()

        else:
            usage_alert()
