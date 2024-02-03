from io import TextIOWrapper
from constans import LOCALHOST, HOSTS_PATH, WEBSITES


class HostsFileManager:

    __hosts_file:TextIOWrapper

    def __init__(self):
        self.__open_hosts_file()
    

    def block_websites(self):
        hosts_file_content = self.__hosts_file.read() 

        non_blocked_websites = self.__get_non_blocked_websites(hosts_file_content)

        self.__append_non_blocked_websites_to_hosts_file(non_blocked_websites)

                
     
    def unblock_websites(self): 
        hosts_file_lines=self.__hosts_file.readlines()

        self.__go_to_beginning_of_hosts_file()

        hosts_file_lines = self.__remove_lines_with_websites_from(hosts_file_lines)

        self.__rewrite_hosts_file_with(hosts_file_lines)
    
        self.__remove_non_overwritten_lines()

    def __open_hosts_file(self):
        with open(HOSTS_PATH, 'r+') as hosts_file:
            self.__hosts_file=hosts_file

    def __get_non_blocked_websites(self,hosts_file_content:str)->[str]:
        return [website for website in WEBSITES if website not in hosts_file_content]
    
    def __append_non_blocked_websites_to_hosts_file(self,non_blocked_websites:[str])->None:
        for website in non_blocked_websites:
            self.__hosts_file.write(LOCALHOST + " " + website + "\n")


    def __go_to_beginning_of_hosts_file(self)->None:
        self.__hosts_file.seek(0)
                
    def __remove_lines_with_websites_from(self, hosts_file_lines:[str])->[str]:
        lines = []

        for line in hosts_file_lines:
            website_is_not_in_line = not any(website in line for website in WEBSITES)

            if website_is_not_in_line:
                lines.append(line)
        
        return lines
    
    def __rewrite_hosts_file_with(self,hosts_file_lines:[str])->None:
        self.__hosts_file.writelines(hosts_file_lines)

    def __remove_non_overwritten_lines(self)->None:
        self.__hosts_file.truncate()

    def close_hosts_file(self):
        self.__hosts_file.close()