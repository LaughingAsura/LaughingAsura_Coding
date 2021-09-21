import jenkins
import os
import time
import sys
import optparse

class Jenkins_Params(object):
    def __init__(self):
        self.server = jenkins.Jenkins("http://10.33.0.159:8080/", username="hx-blr-qa", password="Cisco123")
    
    def get_list_default_params(self, search_string):
        found_job_list = []
        jobs = self.server.get_all_jobs()
        for job in jobs:
            job_info = self.server.get_job_info(job['name'])
            for job_action in job_info['actions']:
                if 'parameterDefinitions' in job_action.keys():
                    for params in job_action['parameterDefinitions']:
                        if 'defaultParameterValue' in params.keys():
                            if 'value' in params['defaultParameterValue'].keys():
                                if search_string in str(params['defaultParameterValue']['value']):
                                    found_job_list.append(job['name'])
        print ('Found Jenkins Jobs : {0}'.format(', '.join(found_job_list)))
        return found_job_list
    
if __name__ == '__main__':
    p = optparse.OptionParser()
    p.add_option("-s", "--search", dest="search_string", help="Search String in Jenkins Job Default Parameters Values..!!", default='')
    opts, args = p.parse_args()
    
    jParam_Obj = Jenkins_Params()
    jParam_Obj.get_list_default_params(opts.search_string)
    