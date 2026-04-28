from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    team_members = [
        {
            "name": "김민수",
            "role": "Backend Developer / Flask 담당",
            "intro": "Flask 기반 서버 구조와 API 설계를 담당하는 백엔드 개발자입니다. 유지보수가 쉬운 아키텍처와 안정적인 API 설계를 중요하게 생각합니다.",
            "contribution": "서버 라우팅, 데이터 처리 로직, Flask 프로젝트 구조 설계 및 API 구현",
            "portfolio": "https://github.com/minsu",
            "email": "minsu@example.com",
            "image": "https://i.pravatar.cc/300?img=12",
            "skills": [
                {"name": "Python", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"},
                {"name": "Flask", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg"},
                {"name": "SQLite", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original.svg"},
                {"name": "GitHub", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg"}
            ]
        },
        {
            "name": "이지현",
            "role": "Frontend Developer / HTML·CSS 담당",
            "intro": "사용자 친화적인 인터페이스와 반응형 웹 디자인을 담당합니다. 심플하면서도 신뢰감 있는 화면 구성을 지향합니다.",
            "contribution": "팀 소개 페이지 UI 설계, 카드 레이아웃 구성, 반응형 디자인 및 스타일 구현",
            "portfolio": "https://github.com/jihyun",
            "email": "jihyun@example.com",
            "image": "https://i.pravatar.cc/300?img=32",
            "skills": [
                {"name": "HTML5", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg"},
                {"name": "CSS3", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg"},
                {"name": "JavaScript", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg"},
                {"name": "Figma", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/figma/figma-original.svg"}
            ]
        },
        {
            "name": "박도윤",
            "role": "DevOps / Nginx·배포 담당",
            "intro": "Nginx, Linux, 배포 자동화를 중심으로 서비스 운영 환경을 구축합니다. 성능과 안정성을 고려한 인프라 구성을 추구합니다.",
            "contribution": "Nginx 리버스 프록시 설정, 배포 환경 구성, Gunicorn 연동 및 운영 관리",
            "portfolio": "https://github.com/doyoon",
            "email": "doyoon@example.com",
            "image": "https://i.pravatar.cc/300?img=45",
            "skills": [
                {"name": "Linux", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg"},
                {"name": "Nginx", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nginx/nginx-original.svg"},
                {"name": "Docker", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg"},
                {"name": "AWS", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/amazonwebservices/amazonwebservices-original-wordmark.svg"}
            ]
        }
    ]

    return render_template("index.html", team_members=team_members)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)