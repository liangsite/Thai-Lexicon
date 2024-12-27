import env

def get_zhongfuyin_silent_rule(output1,output2):
    conditions = {
        ("ก","อา"):"",
        ("ก","อี"):"",
        ("ก","อึอ"):"",
        ("ก","อู"):"",
        ("ก","เอ"):"",
        ("ก","แอ"):"",
        ("ก","โอ"):"",
        ("ก","ออ"):"",
        ("ก","เออ"):"",
        ("จ","อา"):"",
        ("จ","อี"):"",
        ("จ","อึอ"):"",
        ("จ","อู"):"",
        ("จ","เอ"):"",
        ("จ","แอ"):"",
        ("จ","โอ"):"",
        ("จ","ออ"):"",
        ("จ","เออ"):"",

        ("中辅音", "长元音"): "%s (%s) = %s" % (output1, output2,env.sd1),
        ("中辅音", "短元音"): "%s (%s) = %s %s" % (output1, output2,env.sd2, env.yuyinshengdiao[env.sd2]),
        ("中辅音", "特殊元音"): "%s (%s) = %s" % (output1, output2,env.sd1),
        ("中辅音", "短复合元音"): "%s (%s)= %s %s" % (output1,output2, env.sd2, env.yuyinshengdiao[env.sd2]),
        ("中辅音", "长复合元音"): "%s (%s) = %s" % (output1, output2,env.sd1),
        ("中辅音", "长元音", "清尾辅音"): "%s (%s) = %s" % (output1,output2, env.sd1),
        ("中辅音", "长元音", "浊尾辅音"): "%s (%s) = %s %s" % (output1,output2, env.sd2, env.yuyinshengdiao[env.sd2]),
        ("中辅音", "短元音", "清尾辅音"): "%s (%s) = %s" % (output1,output2, env.sd1),
        ("中辅音", "短元音", "浊尾辅音"): "%s (%s) = %s %s" % (output1,output2, env.sd2, env.yuyinshengdiao[env.sd2]),
        ("中辅音", "短复合元音", "清尾辅音"): "%s (%s) = %s" % (output1, output2,env.sd1),
        ("中辅音", "短复合元音", "浊尾辅音"): "%s (%s) = %s %s" % (output1, output2,env.sd2, env.yuyinshengdiao[env.sd2]),
        ("中辅音", "长复合元音", "清尾辅音"): "%s (%s) = %s" % (output1, output2,env.sd1),
        ("中辅音", "长复合元音", "浊尾辅音"): "%s (%s) = %s %s" % (output1, output2,env.sd2, env.yuyinshengdiao[env.sd2]),
    }
    return conditions