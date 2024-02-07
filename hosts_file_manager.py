from io import TextIOWrapper
import time
from constans import LOCALHOST, HOSTS_PATH, WEBSITES


class HostsFileManager:


    def block_websites(self):
        with open(HOSTS_PATH, 'r+') as hosts_file:
            hosts_file_content = hosts_file.read() 

            non_blocked_websites = self.__get_non_blocked_websites(hosts_file_content)

            self.__append_non_blocked_websites_to(hosts_file, non_blocked_websites)

                
     
    def unblock_websites(self): 
        with open(HOSTS_PATH, 'r+') as hosts_file:
            hosts_file_lines=hosts_file.readlines()

            self.__go_to_beginning_of(hosts_file)

            hosts_file_lines = self.__remove_lines_with_websites_from(hosts_file_lines)

            self.__rewrite(hosts_file, hosts_file_lines)
        
            self.__remove_non_overwritten_lines_of(hosts_file)

    def __get_non_blocked_websites(self,hosts_file_content:str)->[str]:
        return [website for website in WEBSITES if website not in hosts_file_content]
    
    @staticmethod
    def __append_non_blocked_websites_to(hosts_file:TextIOWrapper,non_blocked_websites:[str])->None:
        for website in non_blocked_websites:
            hosts_file.write(LOCALHOST + " " + website + "\n")

    @staticmethod
    def __go_to_beginning_of(hosts_file:TextIOWrapper)->None:
        hosts_file.seek(0)
                
    def __remove_lines_with_websites_from(self, hosts_file_lines:[str])->[str]:
        lines = []

        for line in hosts_file_lines:
            website_is_not_in_line = not any(website in line for website in WEBSITES)

            if website_is_not_in_line:
                lines.append(line)
        
        return lines
    
    @staticmethod
    def __rewrite(hosts_file:TextIOWrapper, hosts_file_lines:[str])->None:
        hosts_file.writelines(hosts_file_lines)

    @staticmethod
    def __remove_non_overwritten_lines_of(hosts_file:TextIOWrapper)->None:
        hosts_file.truncate()


if __name__ == "__main__":
    hosts_file_manager = HostsFileManager()
    hosts_file_manager.block_websites()
    print("Blocked")

    time.sleep(30)
    
    hosts_file_manager.unblock_websites()
    print("Unblocked")
