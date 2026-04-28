from flask import Flask, render_template, abort, url_for

app = Flask(__name__)

team_members = [
    {
        "id": 1,
        "name": "김민수",
        "role": "Backend Developer / Flask 담당",
        "intro": "Flask 기반 서버 구조와 API 설계를 담당하는 백엔드 개발자입니다.",
        "detail_intro": (
            "김민수 팀원은 Python과 Flask를 기반으로 웹 애플리케이션의 서버 구조를 설계하고, "
            "사용자 요청을 처리하는 라우팅과 데이터 처리 로직을 담당합니다. "
            "유지보수가 쉬운 코드 구조와 명확한 API 설계를 중요하게 생각합니다."
        ),
        "skills": [
            {"name": "Python", "icon": "bi bi-filetype-py", "short": "PY"},
            {"name": "Flask", "icon": "bi bi-braces", "short": "FL"},
            {"name": "SQLite", "icon": "bi bi-database", "short": "DB"},
            {"name": "GitHub", "icon": "bi bi-github", "short": "GH"}
        ],
        "contribution": "서버 라우팅, Flask 프로젝트 구조 설계, 데이터 처리 로직, 백엔드 기능 구현",
        "portfolio": "https://github.com/minsu",
        "email": "minsu@example.com",
        "image": "images/member1.svg"
    },
    {
        "id": 2,
        "name": "이지현",
        "role": "Frontend Developer / HTML·CSS 담당",
        "intro": "사용자 친화적인 인터페이스와 반응형 웹 디자인을 담당합니다.",
        "detail_intro": (
            "이지현 팀원은 HTML, CSS, Bootstrap을 활용하여 사용자가 보기 쉽고 친근하게 느낄 수 있는 "
            "화면을 구성합니다. 카드형 레이아웃, 반응형 디자인, 색상 조합, 사용자 경험 개선을 담당합니다."
        ),
        "skills": [
            {"name": "HTML5", "icon": "bi bi-filetype-html", "short": "HTML"},
            {"name": "CSS3", "icon": "bi bi-filetype-css", "short": "CSS"},
            {"name": "JavaScript", "icon": "bi bi-filetype-js", "short": "JS"},
            {"name": "Bootstrap", "icon": "bi bi-bootstrap", "short": "BS"}
        ],
        "contribution": "메인 화면 UI 설계, 팀원 카드 디자인, 반응형 레이아웃, Bootstrap 스타일 적용",
        "portfolio": "https://github.com/jihyun",
        "email": "jihyun@example.com",
        "image": "images/member2.svg"
    },
    {
        "id": 3,
        "name": "박도윤",
        "role": "DevOps / Nginx·Waitress 배포 담당",
        "intro": "Nginx와 Windows 서버 환경을 구성하고 안정적인 배포를 담당합니다.",
        "detail_intro": (
            "박도윤 팀원은 Nginx, Waitress, Windows 기반 운영 환경을 구성합니다. "
            "Flask 애플리케이션이 안정적으로 동작할 수 있도록 리버스 프록시, 정적 파일 처리, "
            "배포 환경 설정을 담당합니다."
        ),
        "skills": [
            {"name": "Windows", "icon": "bi bi-windows", "short": "WIN"},
            {"name": "Nginx", "icon": "bi bi-hdd-network", "short": "NG"},
            {"name": "Waitress", "icon": "bi bi-server", "short": "WSGI"},
            {"name": "Deployment", "icon": "bi bi-rocket-takeoff", "short": "DEP"}
        ],
        "contribution": "Nginx 설정, Waitress 연동, Windows 배포 환경 구성, 운영 안정성 관리",
        "portfolio": "https://github.com/doyoon",
        "email": "doyoon@example.com",
        "image": "images/member3.svg"
    }
]


@app.route("/")
def index():
    return render_template(
        "index.html",
        team_members=team_members,
        active_page="home"
    )


@app.route("/members/<int:member_id>")
def member_detail(member_id):
    member = next((m for m in team_members if m["id"] == member_id), None)

    if member is None:
        abort(404)

    return render_template(
        "member_detail.html",
        member=member,
        active_page="members"
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)