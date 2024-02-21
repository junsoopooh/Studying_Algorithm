function solution(park, routes) {
  const N = park.length;
  const M = park[0].length;

  let start;
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      if (park[i][j] == "S") start = [i, j];
    }
  }

  const directions = {
    E: [0, 1],
    W: [0, -1],
    S: [1, 0],
    N: [-1, 0],
  };

  for (const route of routes) {
    const [dir, distanceStr] = route.split(" ");
    let distance = parseInt(distanceStr);
    let [nx, ny] = start;

    let step = 0;
    while (step < distance) {
      nx += directions[dir][0];
      ny += directions[dir][1];

      if (nx < 0 || N <= nx || ny < 0 || M <= ny || park[nx][ny] == "X") break;
      step++;
    }
    if (step == distance) start = [nx, ny];
  }
  return start;
}
