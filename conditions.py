import env

def get_zhongfuyin_silent_rule(output1,output2):
    conditions = {
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


def get_gaofuyin_silent_rule(output1,output2):
    conditions = {
        ("高辅音", "长元音"): "%s (%s) = %s %s" % (output1,output2, env.sd5, env.yuyinshengdiao[env.sd5]),
        ("高辅音", "短元音"): "%s (%s) = %s %s" % (output1,output2, env.sd2, env.yuyinshengdiao[env.sd2]),
        ("高辅音", "特殊元音"): "%s (%s) = %s %s" % (output1,output2, env.sd5, env.yuyinshengdiao[env.sd5]),
        ("高辅音", "短复合元音"): "%s (%s) = %s %s" % (output1,output2, env.sd2, env.yuyinshengdiao[env.sd2]),
        ("高辅音", "长复合元音"): "%s (%s) = %s %s" % (output1,output2, env.sd5, env.yuyinshengdiao[env.sd5]),
        ("高辅音", "长元音", "清尾辅音"): "%s (%s) = %s %s" % (output1,output2, env.sd5, env.yuyinshengdiao[env.sd5]),
        ("高辅音", "长元音", "浊尾辅音"): "%s (%s) = %s %s" % (output1,output2, env.sd2, env.yuyinshengdiao[env.sd2]),
        ("高辅音", "短元音", "清尾辅音"): "%s (%s) = %s %s" % (output1,output2, env.sd5, env.yuyinshengdiao[env.sd5]),
        ("高辅音", "短元音", "浊尾辅音"): "%s (%s) = %s %s" % (output1,output2, env.sd2, env.yuyinshengdiao[env.sd2]),
        ("高辅音", "短复合元音", "清尾辅音"): "%s (%s) = %s %s" % (output1,output2, env.sd5, env.yuyinshengdiao[env.sd5]),
        ("高辅音", "短复合元音", "浊尾辅音"): "%s (%s) = %s %s" % (output1,output2, env.sd2, env.yuyinshengdiao[env.sd2]),
        ("高辅音", "长复合元音", "清尾辅音"): "%s (%s) = %s %s" % (output1,output2, env.sd5, env.yuyinshengdiao[env.sd5]),
        ("高辅音", "长复合元音", "浊尾辅音"): "%s (%s) = %s %s" % (output1,output2, env.sd2, env.yuyinshengdiao[env.sd2]),
    }
    return conditions

def get_difuyin_silent_rule(output1,output2):
    condition = {
        ("低辅音", "长元音"): "%s (%s) = %s" % (output1,output2, env.sd1),
        ("低辅音", "短元音"): "%s (%s) = %s %s" % (output1,output2, env.sd4, env.yuyinshengdiao[env.sd4]),
        ("低辅音", "特殊元音"): "%s (%s) = %s" % (output1,output2, env.sd1),
        ("低辅音", "短复合元音"): "%s (%s) = %s %s" % (output1,output2, env.sd4, env.yuyinshengdiao[env.sd4]),
        ("低辅音", "长复合元音"): "%s (%s) = %s" % (output1, output2,env.sd1),
        ("低辅音", "长元音", "清尾辅音"): "%s (%s) = %s" % (output1,output2, env.sd1),
        ("低辅音", "长元音", "浊尾辅音"): "%s (%s) = %s %s" % (output1,output2, env.sd3, env.yuyinshengdiao[env.sd3]),
        ("低辅音", "短元音", "清尾辅音"): "%s (%s) = %s" % (output1,output2, env.sd1),
        ("低辅音", "短元音", "浊尾辅音"): "%s (%s) = %s %s" % (output1,output2, env.sd4, env.yuyinshengdiao[env.sd4]),
        ("低辅音", "短复合元音", "清尾辅音"): "%s (%s) = %s" % (output1,output2, env.sd1),
        ("低辅音", "短复合元音", "浊尾辅音"): "%s (%s) = %s %s" % (output1,output2, env.sd4, env.yuyinshengdiao[env.sd4]),
        ("低辅音", "长复合元音", "清尾辅音"): "%s (%s) = %s" % (output1,output2, env.sd1),
        ("低辅音", "长复合元音", "浊尾辅音"): "%s (%s) = %s %s" % (output1,output2, env.sd3, env.yuyinshengdiao[env.sd3]),
    }
    return condition


def get_zhongfuyin_tone_rule(output1,output2):
    conditions = {
        ("中辅音", "长元音", "第2声调"): "%s (%s) = %s %s" % (output1,output2,env.sd2, env.yuyinshengdiao[env.sd2]),
        ("中辅音", "长元音", "第3声调"): "%s (%s) = %s %s" % (output1,output2, env.sd3, env.yuyinshengdiao[env.sd3]),
        ("中辅音", "长元音", "第4声调"): "%s (%s) = %s %s" % (output1,output2, env.sd4, env.yuyinshengdiao[env.sd4]),
        ("中辅音", "长元音", "第5声调"): "%s (%s) = %s %s" % (output1,output2, env.sd5, env.yuyinshengdiao[env.sd5]),
        ("中辅音", "短元音", "第3声调"): "%s (%s) = %s %s" % (output1,output2, env.sd3, env.yuyinshengdiao[env.sd3]),
        ("中辅音", "短元音", "第4声调"): "%s (%s) = %s %s" % (output1,output2, env.sd4, env.yuyinshengdiao[env.sd4]),
        ("中辅音", "短元音", "第5声调"): "%s (%s) = %s %s" % (output1,output2, env.sd5, env.yuyinshengdiao[env.sd5]),
        ("中辅音", "特殊元音", "第2声调"): "%s (%s) = %s %s" % (output1,output2, env.sd2, env.yuyinshengdiao[env.sd2]),
        ("中辅音", "特殊元音", "第3声调"): "%s (%s) = %s %s" % (output1,output2, env.sd3, env.yuyinshengdiao[env.sd3]),
        ("中辅音", "特殊元音", "第4声调"): "%s (%s) = %s %s" % (output1,output2, env.sd4, env.yuyinshengdiao[env.sd4]),
        ("中辅音", "特殊元音", "第5声调"): "%s (%s) = %s %s" % (output1,output2, env.sd5, env.yuyinshengdiao[env.sd5]),
        ("中辅音", "短复合元音", "第3声调"): "%s (%s) = %s %s" % (output1,output2, env.sd3, env.yuyinshengdiao[env.sd3]),
        ("中辅音", "短复合元音", "第4声调"): "%s (%s) = %s %s" % (output1,output2, env.sd4, env.yuyinshengdiao[env.sd4]),
        ("中辅音", "短复合元音", "第5声调"): "%s (%s) = %s %s" % (output1,output2, env.sd5, env.yuyinshengdiao[env.sd5]),
        ("中辅音", "长复合元音", "第2声调"): "%s (%s) = %s %s" % (output1,output2, env.sd2, env.yuyinshengdiao[env.sd2]),
        ("中辅音", "长复合元音", "第3声调"): "%s (%s) = %s %s" % (output1,output2, env.sd3, env.yuyinshengdiao[env.sd3]),
        ("中辅音", "长复合元音", "第4声调"): "%s (%s) = %s %s" % (output1,output2, env.sd4, env.yuyinshengdiao[env.sd4]),
        ("中辅音", "长复合元音", "第5声调"): "%s (%s) = %s %s" % (output1,output2, env.sd5, env.yuyinshengdiao[env.sd5]),
        ("中辅音", "长元音", "清尾辅音", "第2声调"): "%s (%s) = %s %s" % (output1,output2, env.sd2, env.yuyinshengdiao[env.sd2]),
        ("中辅音", "长元音", "清尾辅音", "第3声调"): "%s (%s) = %s %s" % (output1,output2, env.sd3, env.yuyinshengdiao[env.sd3]),
        ("中辅音", "长元音", "清尾辅音", "第4声调"): "%s (%s) = %s %s" % (output1,output2, env.sd4, env.yuyinshengdiao[env.sd4]),
        ("中辅音", "长元音", "清尾辅音", "第5声调"): "%s (%s) = %s %s" % (output1,output2, env.sd5, env.yuyinshengdiao[env.sd5]),
        ("中辅音", "长元音", "浊尾辅音", "第2声调"): "%s (%s) = %s %s" % (output1,output2, env.sd2, env.yuyinshengdiao[env.sd2]),
        ("中辅音", "长元音", "浊尾辅音", "第3声调"): "%s (%s) = %s %s" % (output1,output2, env.sd3, env.yuyinshengdiao[env.sd3]),
        ("中辅音", "长元音", "浊尾辅音", "第4声调"): "%s (%s) = %s %s" % (output1,output2, env.sd4, env.yuyinshengdiao[env.sd4]),
        ("中辅音", "长元音", "浊尾辅音", "第5声调"): "%s (%s) = %s %s" % (output1,output2, env.sd5, env.yuyinshengdiao[env.sd5]),
        ("中辅音", "短元音", "清尾辅音", "第3声调"): "%s (%s) = %s %s" % (output1,output2, env.sd3, env.yuyinshengdiao[env.sd3]),
        ("中辅音", "短元音", "清尾辅音", "第4声调"): "%s (%s) = %s %s" % (output1,output2, env.sd4, env.yuyinshengdiao[env.sd4]),
        ("中辅音", "短元音", "清尾辅音", "第5声调"): "%s (%s) = %s %s" % (output1,output2, env.sd5, env.yuyinshengdiao[env.sd5]),
        ("中辅音", "短元音", "浊尾辅音", "第3声调"): "%s (%s) = %s %s" % (output1,output2, env.sd3, env.yuyinshengdiao[env.sd3]),
        ("中辅音", "短元音", "浊尾辅音", "第4声调"): "%s (%s) = %s %s" % (output1,output2, env.sd4, env.yuyinshengdiao[env.sd4]),
        ("中辅音", "短元音", "浊尾辅音", "第5声调"): "%s (%s) = %s %s" % (output1,output2, env.sd5, env.yuyinshengdiao[env.sd5]),
        ("中辅音", "短复合元音", "清尾辅音", "第3声调"): "%s (%s) = %s %s" % (output1,output2, env.sd3, env.yuyinshengdiao[env.sd3]),
        ("中辅音", "短复合元音", "清尾辅音", "第4声调"): "%s (%s) = %s %s" % (output1,output2, env.sd4, env.yuyinshengdiao[env.sd4]),
        ("中辅音", "短复合元音", "清尾辅音", "第5声调"): "%s (%s) = %s %s" % (output1,output2, env.sd5, env.yuyinshengdiao[env.sd5]),
        ("中辅音", "短复合元音", "浊尾辅音", "第3声调"): "%s (%s) = %s %s" % (output1,output2, env.sd3, env.yuyinshengdiao[env.sd3]),
        ("中辅音", "短复合元音", "浊尾辅音", "第4声调"): "%s (%s) = %s %s" % (output1,output2, env.sd4, env.yuyinshengdiao[env.sd4]),
        ("中辅音", "短复合元音", "浊尾辅音", "第5声调"): "%s (%s) = %s %s" % (output1,output2, env.sd5, env.yuyinshengdiao[env.sd5]),
        ("中辅音", "长复合元音", "清尾辅音", "第2声调"): "%s (%s) = %s %s" % (output1,output2, env.sd2, env.yuyinshengdiao[env.sd2]),
        ("中辅音", "长复合元音", "清尾辅音", "第3声调"): "%s (%s) = %s %s" % (output1,output2, env.sd3, env.yuyinshengdiao[env.sd3]),
        ("中辅音", "长复合元音", "清尾辅音", "第4声调"): "%s (%s) = %s %s" % (output1,output2, env.sd4, env.yuyinshengdiao[env.sd4]),
        ("中辅音", "长复合元音", "清尾辅音", "第5声调"): "%s (%s) = %s %s" % (output1,output2, env.sd5, env.yuyinshengdiao[env.sd5]),
        ("中辅音", "长复合元音", "浊尾辅音", "第3声调"): "%s (%s) = %s %s" % (output1,output2, env.sd3, env.yuyinshengdiao[env.sd3]),
        ("中辅音", "长复合元音", "浊尾辅音", "第4声调"): "%s (%s) = %s %s" % (output1,output2, env.sd4, env.yuyinshengdiao[env.sd4]),
        ("中辅音", "长复合元音", "浊尾辅音", "第5声调"): "%s (%s) = %s %s" % (output1,output2, env.sd5, env.yuyinshengdiao[env.sd5]),
    }
    return conditions


def get_gaofuyin_tone_rule(output1,output2):
    conditions = {
        ("高辅音", "长元音", "第2声调"): "%s (%s) = %s %s" % (output1,output2, env.sd2, env.yuyinshengdiao[env.sd2]),
        ("高辅音", "长元音", "第3声调"): "%s (%s) = %s %s" % (output1,output2, env.sd3, env.yuyinshengdiao[env.sd3]),
        ("高辅音", "短元音", "第3声调"): "%s (%s) = %s %s" % (output1,output2, env.sd3, env.yuyinshengdiao[env.sd3]),
        ("高辅音", "特殊元音", "第2声调"): "%s (%s) = %s %s" % (output1,output2, env.sd2, env.yuyinshengdiao[env.sd2]),
        ("高辅音", "特殊元音", "第3声调"): "%s (%s) = %s %s" % (output1,output2, env.sd3, env.yuyinshengdiao[env.sd3]),
        ("高辅音", "短复合元音", "第3声调"): "%s (%s) = %s %s" % (output1,output2, env.sd3, env.yuyinshengdiao[env.sd3]),
        ("高辅音", "长复合元音", "第2声调"): "%s (%s) = %s %s" % (output1,output2, env.sd2, env.yuyinshengdiao[env.sd2]),
        ("高辅音", "长复合元音", "第3声调"): "%s (%s) = %s %s" % (output1,output2, env.sd3, env.yuyinshengdiao[env.sd3]),
        ("高辅音", "长元音", "清尾辅音", "第2声调"): "%s (%s) = %s %s" % (output1,output2, env.sd2, env.yuyinshengdiao[env.sd2]),
        ("高辅音", "长元音", "清尾辅音", "第3声调"): "%s (%s) = %s %s" % (output1,output2, env.sd3, env.yuyinshengdiao[env.sd3]),
        ("高辅音", "长元音", "浊尾辅音", "第2声调"): "%s (%s) = %s %s" % (output1,output2, env.sd2, env.yuyinshengdiao[env.sd2]),
        ("高辅音", "长元音", "浊尾辅音", "第3声调"): "%s (%s) = %s %s" % (output1,output2, env.sd3, env.yuyinshengdiao[env.sd3]),
        ("高辅音", "短元音", "清尾辅音", "第3声调"): "%s (%s) = %s %s" % (output1,output2, env.sd3, env.yuyinshengdiao[env.sd3]),
        ("高辅音", "短元音", "浊尾辅音", "第3声调"): "%s (%s) = %s %s" % (output1,output2, env.sd3, env.yuyinshengdiao[env.sd3]),
        ("高辅音", "短复合元音", "清尾辅音", "第3声调"): "%s (%s) = %s %s" % (output1,output2, env.sd3, env.yuyinshengdiao[env.sd3]),
        ("高辅音", "短复合元音", "浊尾辅音", "第3声调"): "%s (%s) = %s %s" % (output1,output2, env.sd3, env.yuyinshengdiao[env.sd3]),
        ("高辅音", "长复合元音", "清尾辅音", "第2声调"): "%s (%s) = %s %s" % (output1,output2, env.sd2, env.yuyinshengdiao[env.sd2]),
        ("高辅音", "长复合元音", "清尾辅音", "第3声调"): "%s (%s) = %s %s" % (output1,output2, env.sd3, env.yuyinshengdiao[env.sd3]),
        ("高辅音", "长复合元音", "浊尾辅音", "第3声调"): "%s (%s) = %s %s" % (output1,output2, env.sd3, env.yuyinshengdiao[env.sd3]),
    }
    return conditions


def get_difuyin_tone_rule(output1,output2):
    conditions = {
        ("低辅音", "长元音", "第2声调"): "%s (%s) = %s %s" % (output1,output2, env.sd3, env.yuyinshengdiao[env.sd3]),
        ("低辅音", "长元音", "第3声调"): "%s (%s) = %s %s" % (output1,output2, env.sd4, env.yuyinshengdiao[env.sd4]),
        ("低辅音", "短元音", "第2声调"): "%s (%s) = %s %s" % (output1,output2, env.sd3, env.yuyinshengdiao[env.sd3]),
        ("低辅音", "特殊元音", "第2声调"): "%s (%s) = %s %s" % (output1,output2, env.sd3, env.yuyinshengdiao[env.sd3]),
        ("低辅音", "特殊元音", "第3声调"): "%s (%s) = %s %s" % (output1,output2, env.sd4, env.yuyinshengdiao[env.sd4]),
        ("低辅音", "短复合元音", "第2声调"): "%s (%s) = %s %s" % (output1,output2, env.sd3, env.yuyinshengdiao[env.sd3]),
        ("低辅音", "长复合元音", "第2声调"): "%s (%s) = %s %s" % (output1,output2, env.sd2, env.yuyinshengdiao[env.sd2]),
        ("低辅音", "长复合元音", "第3声调"): "%s (%s) = %s %s" % (output1,output2, env.sd3, env.yuyinshengdiao[env.sd3]),
        ("低辅音", "长元音", "清尾辅音", "第2声调"): "%s (%s) = %s %s" % (output1,output2, env.sd3, env.yuyinshengdiao[env.sd3]),
        ("低辅音", "长元音", "清尾辅音", "第3声调"): "%s (%s) = %s %s" % (output1,output2, env.sd4, env.yuyinshengdiao[env.sd4]),
        ("低辅音", "长元音", "浊尾辅音", "第2声调"): "%s (%s) = %s %s" % (output1,output2, env.sd3, env.yuyinshengdiao[env.sd3]),
        ("低辅音", "长元音", "浊尾辅音", "第3声调"): "%s (%s) = %s %s" % (output1,output2, env.sd4, env.yuyinshengdiao[env.sd4]),
        ("低辅音", "短元音", "清尾辅音", "第2声调"): "%s (%s) = %s %s" % (output1,output2, env.sd3, env.yuyinshengdiao[env.sd3]),
        ("低辅音", "短元音", "清尾辅音", "第3声调"): "%s (%s) = %s %s" % (output1,output2, env.sd4, env.yuyinshengdiao[env.sd4]),
        ("低辅音", "短复合元音", "浊尾辅音", "第3声调"): "%s (%s) = %s %s" % (output1,output2, env.sd4, env.yuyinshengdiao[env.sd4]),
        ("低辅音", "长复合元音", "清尾辅音", "第2声调"): "%s (%s) = %s %s" % (output1,output2, env.sd3, env.yuyinshengdiao[env.sd3]),
        ("低辅音", "长复合元音", "清尾辅音", "第3声调"): "%s (%s) = %s %s" % (output1,output2, env.sd4, env.yuyinshengdiao[env.sd4]),
        ("低辅音", "长复合元音", "浊尾辅音", "第3声调"): "%s (%s) = %s %s" % (output1,output2, env.sd4, env.yuyinshengdiao[env.sd4]),
    }
    return conditions