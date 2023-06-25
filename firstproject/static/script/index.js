function goToDetail(postId) {
    // postId를 사용하여 상세화면 URL을 생성
    var detailUrl = "/posting/" + postId;

    // 상세화면으로 이동
    window.location.href = detailUrl;
  }