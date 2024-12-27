import streamlit as st
import env
import conditions

st.title("泰语声调公式查询")
with st.expander("关于泰语声调查询"):
    st.markdown(
        """
        由于本人是初学者，对于声调公式逻辑完全都是从基础泰语书里以及泰国朋友凤凤结合写的。
        暂时没有前引字、复合辅音之类或者复杂的单词的声调查询......后续会有的。哈哈哈哈哈
        
        关于没有结果显示......那就是没有。如果有但是没有结果显示或者对公式有任何问题可[私信我](https://ergua.cc)修改。
        在此，真诚的感谢您宝贵的意见！

        如果你要查的单词忘记变形前的元音字母，可在这里查看：
        """
    )
    st.image("https://images.ergua.cc/images/thai_rule.jpg", caption="清尾辅音变形规则")


opts = {}
col1,col2,col3 = st.columns(3)
with col1:
    opts_fuyin = st.selectbox(
        "辅音字母",env.fuyin.keys(),index=None
    )

    if opts_fuyin:
        opts_fuyin_thai = st.selectbox(
            "非必选项",env.fuyin[opts_fuyin],index=None
        )
        if opts_fuyin_thai:
            opts[opts_fuyin_thai] = opts_fuyin_thai

with col2:
    opts_yuanyin = st.selectbox(
        "元音字母",env.yuanyin.keys(),index=None
    )
    if opts_yuanyin:
        opts_yuanyin_thai = st.selectbox(
            "非必选项",env.yuanyin[opts_yuanyin],index=None
        )
        if opts_yuanyin_thai:
            opts[opts_yuanyin_thai] = opts_yuanyin_thai

with col3:
    opts_weifuyin = st.selectbox(
        "尾辅音字母",env.weifuyin.keys(),index=None
    )
    if opts_weifuyin:
        opts_weifuyin_thai = st.selectbox(
                "非必选项",env.weifuyin[opts_weifuyin],index=None
        )
        if opts_weifuyin_thai:
            opts[opts_weifuyin_thai] = opts_weifuyin_thai

col4,col5 = st.columns(2)
with col4:
    on = st.toggle("声调(可选)")
    if on:
        opts_shengdiao = st.selectbox(
            "非必选项",
            env.yuyinshengdiao.keys(),index=None,
            label_visibility="collapsed"
        )
        # if opts_shengdiao is not None:
        #if opts_shengdiao:
        #    opts[opts_shengdiao] = env.yuyinshengdiao[opts_shengdiao]
    else:
        opts_shengdiao=None


with col5:
    optts1 = [option1 for option1 in [opts_fuyin,opts_yuanyin,opts_weifuyin,opts_shengdiao] if option1 is not None]
    optts2 = [option2 for option2 in opts.keys() if option2 is not None]
    output1 = '+'.join(optts1)
    output2 = "+".join(optts2)
    st.write("选中预览")
    st.success(f"{output1} {output2}")
    



if opts_fuyin == "中辅音" and on == False:
    # 根据选项匹配字典中的条件
    call = conditions.get_zhongfuyin_silent_rule(output1,output2)
    result = call.get(tuple(optts1), "未匹配任何情况")
    if result != "未匹配任何情况":
        st.write("结果展示：")
        st.info(result)

elif opts_fuyin == "高辅音" and on == False:
    call = conditions.get_gaofuyin_silent_rule(output1,output2)
    result = call.get(tuple(optts1), "未匹配任何情况")
    if result != "未匹配任何情况":
        st.write("结果展示：")
        st.info(result)

elif opts_fuyin == "低辅音" and on == False:
    call = conditions.get_difuyin_silent_rule(output1,output2)
    result = call.get(tuple(optts1), "未匹配任何情况")
    if result != "未匹配任何情况":
        st.write("结果展示：")
        st.info(result)

elif opts_fuyin == "中辅音" and on == True:
    call = conditions.get_zhongfuyin_tone_rule(output1,output2)
    result = call.get(tuple(optts1), "未匹配任何情况")
    if result != "未匹配任何情况":
        st.write("结果展示：")
        st.info(result)

elif opts_fuyin == "高辅音" and on == True:
    call = conditions.get_gaofuyin_tone_rule(output1,output2)
    result = call.get(tuple(optts1), "未匹配任何情况")
    if result != "未匹配任何情况":
        st.write("结果展示：")
        st.info(result)

elif opts_fuyin == "低辅音" and on == True:
    call = conditions.get_difuyin_tone_rule(output1,output2)
    result = call.get(tuple(optts1), "未匹配任何情况")
    if result != "未匹配任何情况":
        st.write("结果展示：")
        st.info(result)