# Clone

```bash
$ git clone https://github.com/kdt-live/TIL.git
```

* 상위폴더에 git init이 안된 경로에서 clone하도록 하자.
* 이후 업데이트가 있을시 다음 명령어로 가져오자.

```bash
$ git pull origin master
```



## 전체적인 흐름 

```bash
# 로컬
$ git init
$ git add .
$ git commit -m '메시지'
$ git status
$ git log

#원격
$ git push origin master
$ git pull origin master
$ git remote add origin [link]
$ git clone [link]
```



# 협업

![image-20220707131915257](2022_07_07_GitGithubNotes.assets/image-20220707131915257.png)

* 개별적으로 나눠진 각 branch에서 작업을 진행하고, merge해서 master branch에 업데이트를 하는 형식으로 분업이 진행된다.



## 형태

1. Feature Branch Workflow

   * Shared repository model (저장소의 소유권이 있는 경우)

2. Forking Workflow

   * Fork & Pull model (저장소의 소유권이 없는 경우)

   

## Branch 명명

| Branch                        | 주요 특징                                                    |
| :---------------------------- | ------------------------------------------------------------ |
| master (main)                 | 배포 가능한 상태의 코드                                      |
| develop (main)                | feature branch로 나뉘어지거나, 발생된 버그 수정 등 개발 진행<br />개발 이후 release branch로 갈라짐 |
| feature branches (supporting) | 기능별 개발 브랜치(topic branch)<br />기능이 반영되거나 드랍되는 경우 브랜치 삭제 |
| release branches (supporting) | 개발 완료 이후 QA/Test 등을 통해 얻어진 다음 배포 전 minor bug fix등 반영 |
| hotfixes (supporting)         | 긴급하게 반영 해야하는 bug fix<br />release branch는 다음 버전을 위한 것 이라면 hotfix branch는 현재 버전을 위한것 |



# Branch

```bash
#브랜치 생성
$ git branch [브랜치이름]

#브랜치 조회
$ git branch

#브랜치 이동
$ git checkout [브랜치명]
$ git checkout -b [브랜치명] # 브랜치 생성후 이동하기

#브랜치 삭제
$ git branch -d [브랜치명]

#브랜치 병합(merge)
$ git merge [브랜치명]
$ git merge [브랜치명] --edit #병합 후 바로 편집기가 나오면서 커밋 메시지 수정 가능
$ git merge [브랜치명] --no-edit #커밋 메시지 수정없이 바로 병합

```

