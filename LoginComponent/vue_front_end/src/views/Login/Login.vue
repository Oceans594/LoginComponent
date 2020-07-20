<template>
  <div class="login" :style="styleSet">
    <div class="login-form">
      <div class="login-header">
        <p>斗鱼业务管理平台</p>
      </div>
      <el-form :model="ruleForm" :rules="rules" ref="ruleForm">
        <el-form-item prop="username">
          <el-input placeholder="请输入用户名" prefix-icon="el-icon-user" v-model="ruleForm.username">
          </el-input>
        </el-form-item>
        <el-form-item prop="password">
        <el-input placeholder="请输入密码" type="password" prefix-icon="el-icon-lock" v-model="ruleForm.password">
        </el-input>
        </el-form-item>
        <el-button type="primary" @click="Submit('ruleForm')" style="width: 100%;margin-bottom: 18px">登录</el-button>
        <div>
          <el-checkbox v-model="ruleForm.checked">记住我</el-checkbox>
        </div>
      </el-form>
    </div>
  </div>
</template>

<script>
import { Message } from 'element-ui'
export default {
  data () {
    return {
      ruleForm: {
        checked: true,
        username: '',
        password: ''
      },
      styleSet: {
        backgroundImage: 'url(' + require('../../assets/bg.png') + ')',
        backgroundRepeat: 'no-repeat',
        backgroundSize: '100% 100%'
      },
      rules: {
        username: [
          { required: true, message: '请输入用户名', trigger: 'blur' },
          { min: 2, max: 10, message: '长度2~10个字符', trigger: 'blur' },
          { required: true, pattern: /^[\u4e00-\u9fa5_a-zA-Z0-9.·-]+$/, message: '用户名不支持特殊字符', trigger: 'blur' }
        ],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' },
          { min: 6, max: 16, message: '长度6~16个字符', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    Submit: function (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.$axios.post('/auth/login', {
            username: this.ruleForm.username, password: this.ruleForm.password, isRemember: this.ruleForm.checked
          }).then(response => {
            if (response.data.Error) {
              Message({
                type: 'error',
                message: response.data.Error,
                duration: 1500
              })
            } else {
              this.$router.push('/home')
            }
          })
        } else {
          console.log('error submit!!')
          return false
        }
      })
    }
  }
}
</script>

<style lang="less" scoped>
  @import "Login.less";
</style>
