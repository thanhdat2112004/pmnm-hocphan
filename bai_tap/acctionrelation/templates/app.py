from datetime import timedelta
from flask import Flask, flash, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = 'khoa_bi_mat_cho_session'

# Danh sách tài khoản cho trước
USERS = {
    "admin": "admin123",
    "an": "an123456"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Nếu đã đăng nhập rồi mà truy cập /login thì chuyển về trang chủ
    if 'user' in session:
        return redirect(url_for('index'))
        
    username = ''
    if request.method == 'POST':
        # Xử lý cắt khoảng trắng tên đăng nhập (.strip())
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        remember = request.form.get('remember') # Ô ghi nhớ đăng nhập

        # Kiểm tra thông tin tài khoản (phân biệt hoa thường)
        if username in USERS and USERS[username] == password:
            session['user'] = username
            
            # Xử lý tính năng "Ghi nhớ đăng nhập"
            if remember:
                session.permanent = True
                app.permanent_session_lifetime = timedelta(days=7)
            else:
                session.permanent = False
                
            flash(f"Đăng nhập thành công. Xin chào {username}!", "success")
            return redirect(url_for('index'))
        else:
            flash("Sai tên đăng nhập hoặc mật khẩu.", "danger")
            # Giữ lại tên đăng nhập, không giữ mật khẩu

    return render_template('login.html', username=username)

@app.route('/profile')
def profile():
    # Kiểm tra xem đã đăng nhập chưa
    if 'user' not in session:
        flash("Vui lòng đăng nhập để tiếp tục.", "warning")
        return redirect(url_for('login'))
    return render_template('profile.html', user=session['user'])

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    # Xóa session để đăng xuất
    session.pop('user', None)
    flash("Bạn đã đăng xuất.", "info")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)