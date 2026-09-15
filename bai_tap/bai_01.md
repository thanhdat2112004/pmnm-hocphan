BÀI 1.1: HOÀN THIỆN FILE README.md
Bạn mở file README.md trong thư mục pmnm-hocphan trên máy tính, dán nội dung dưới đây vào, điền đầy đủ thông tin cá nhân rồi commit và push lên GitHub:

Markdown
# Kho mã môn học: Phần mềm mã nguồn mở (pmnm-hocphan)

## Thông tin sinh viên
Họ và tên: Phạm Đức Thành Đạt
Mã sinh viên: 22T1020058
Lớp: I / Ngành công nghệ thông tin

## Lý do tôi muốn học về Phần mềm Mã nguồn mở

Là một sinh viên ngành Công nghệ Thông tin, việc học về phần mềm mã nguồn mở đóng vai trò quan trọng trong việc định hình tư duy phát triển phần mềm và xây dựng kỹ năng chuyên môn. Việc tiếp cận mã nguồn mở giúp tôi không chỉ hiểu sâu hơn về cách các hệ thống lớn được kiến trúc và vận hành trong thực tế, mà còn học hỏi được tư duy tối ưu hóa code từ cộng đồng lập trình viên quốc tế. 

Bên cạnh đó, văn hóa mã nguồn mở khuyến khích sự chia sẻ, tái sử dụng và hợp tác – những kỹ năng cốt lõi giúp tôi làm việc hiệu quả hơn trong các dự án thực tế. Việc chủ động tham gia, sử dụng và đóng góp cho các dự án mở cũng giúp tôi rèn luyện kỹ năng kiểm soát phiên bản với Git/GitHub, đồng thời xây dựng một hồ sơ năng lực (portfolio) thực tế và uy tín để chuẩn bị cho cơ hội nghề nghiệp trong tương lai.

---

## Danh sách 5 phần mềm mã nguồn mở đang sử dụng hằng ngày

1. **Linux (Ubuntu / Fedora / Arch Linux)**
   * *Giấy phép:* GNU General Public License v2 (GPLv2)
2. **Visual Studio Code (Bản core / VSCodium)**
   * *Giấy phép:* MIT License (cho phần mã nguồn core trên GitHub)
3. **GIMP (GNU Image Manipulation Program)**
   * *Giấy phép:* GNU General Public License v3 (GPLv3)
4. **PostgreSQL**
   * *Giấy phép:* PostgreSQL License (giấy phép dạng permissive, tương tự MIT/BSD)
5. **OBS Studio (Open Broadcaster Software)**
   * *Giấy phép:* GNU General Public License v2 (GPLv2)
BÀI 1.2: BÁO CÁO PHÂN TÍCH SỰ BẤT HÒA CỘNG ĐỒNG VÀ SỰ RẼ NHÁNH (FORK): TRƯỜNG HỢP MYSQL VÀ MARIADB
Bạn có thể tạo một file mới tên là BAOCAO_BAI1.2.md hoặc REPORT.md trong cùng repository pmnm-hocphan để lưu trữ nội dung bài báo cáo dưới đây (độ dài khoảng ~600 từ):

BÁO CÁO PHÂN TÍCH: SỰ RẼ NHÁNH CỦA MARIADB TỪ MYSQL
1. Giới thiệu tổng quan
Trong lịch sử phát triển của phần mềm mã nguồn mở, dự án cơ sở dữ liệu quan hệ MySQL là một trong những trường hợp điển hình nhất về sự xung đột lợi ích giữa định hướng quản trị thương mại và triết lý cộng đồng. Việc thương vụ thâu tóm diễn ra liên tiếp đã dẫn đến hành động rẽ nhánh (fork) tạo nên MariaDB – một hệ quản trị cơ sở dữ liệu mã nguồn mở hoàn toàn tách biệt nhưng tương thích ngược với MySQL.

2. Nguyên nhân và bối cảnh mâu thuẫn
MySQL ban đầu được phát triển bởi công ty MySQL AB (Thụy Điển) dưới triết lý mã nguồn mở GPL. Năm 2008, Sun Microsystems mua lại MySQL AB. Tuy nhiên, biến cố lớn nhất xảy ra vào năm 2009–2010 khi tập đoàn Oracle tiến hành thâu tóm Sun Microsystems, qua đó nắm quyền sở hữu trực tiếp đối với dự án MySQL.

Sự kiện này gây ra làn sóng lo ngại sâu sắc trong cộng đồng mã nguồn mở:

Xung đột lợi ích cốt lõi: Oracle vốn sở hữu sản phẩm cơ sở dữ liệu thương mại đóng đắt đỏ (Oracle Database). Cộng đồng lo ngại Oracle sẽ cố tình làm suy yếu MySQL để tránh cạnh tranh trực tiếp với sản phẩm chủ lực của họ.

Mất niềm tin vào tính minh bạch: Các nhà phát triển lo ngại Oracle sẽ dần khép kín các tính năng cao cấp (chuyển sang mô hình Open Core), thắt chặt quyền đóng góp mã nguồn và thay đổi chính sách giấy phép theo hướng bất lợi cho người dùng tự do.

3. Diễn biến rẽ nhánh (Forking)
Đứng trước nguy cơ dự án bị thao túng, Michael "Monty" Widenius – tác giả chính và là đồng sáng lập của MySQL AB – đã quyết định rời khỏi Sun/Oracle để thành lập dự án MariaDB vào năm 2009.

MariaDB được thiết kế để làm bản thế chân hoàn hảo (drop-in replacement) cho MySQL, nghĩa là người dùng có thể thay thế MySQL bằng MariaDB mà không cần thay đổi cấu trúc truy vấn hay mã nguồn ứng dụng. Để bảo vệ tính độc lập, Widenius thành lập MariaDB Foundation – một tổ chức phi lợi nhuận chịu trách nhiệm định hướng và phát triển dự án, đảm bảo mã nguồn MariaDB luôn giữ đúng tinh thần mở dưới giấy phép GNU GPL.

4. Kết quả và tác động đến hệ sinh thái
Việc rẽ nhánh MariaDB đã mang lại những ảnh hưởng to lớn cho cộng đồng hạ tầng phần mềm:

Sự dịch chuyển của các hệ điều hành lớn: Nhiều bản phân phối Linux hàng đầu như Red Hat Enterprise Linux (RHEL), CentOS, Debian và Arch Linux đã quyết định loại bỏ MySQL để chọn MariaDB làm hệ quản trị cơ sở dữ liệu mặc định.

Tác động đến Oracle MySQL: Nhờ có áp lực cạnh tranh từ MariaDB, Oracle buộc phải tiếp tục duy trì và nâng cấp MySQL (đặc biệt là phiên bản MySQL 8.0) thay vì khai tử hay đóng kín hoàn toàn như lo ngại ban đầu.

Động lực đổi mới: MariaDB đã giới thiệu nhiều công cụ lưu trữ (storage engines) mới tối ưu hơn như Aria, ColumnStore và cải thiện hiệu năng xử lý truy vấn song song tốt hơn so với các bản MySQL cùng thời điểm.

5. Bài học rút ra
Trường hợp giữa MySQL và MariaDB cung cấp một bài học đắt giá về sức mạnh của cơ chế "Fork" trong mã nguồn mở. Khi một doanh nghiệp tìm cách độc quyền hoặc đe dọa sự phát triển tự do của một dự án, cộng đồng hoàn toàn có quyền và đủ khả năng tạo ra một hướng đi mới để bảo vệ sản phẩm chung. Quyền rẽ nhánh chính là "van an toàn" tối thượng, đảm bảo giá trị của phần mềm mã nguồn mở luôn thuộc về cộng đồng thay bị phụ thuộc vào quyết định của bất kỳ tập đoàn thương mại nào.
