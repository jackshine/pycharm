# encoding=utf-8

if __name__=="__main__":
    qrm_client_accout = {}
    for line in open('./qrm_client_account.txt'):
        list = line.split('=')
        qrm_client_accout[list[0]] = list[1].strip()
    print(qrm_client_accout)
    mz_login_account = {}
    for line in open('./mz_login_account.txt'):
        list = line.split('=')
        mz_login_account[list[0]] = list[1].strip()
    print(mz_login_account)