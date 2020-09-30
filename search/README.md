# Mô tả cách làm

## Bài 1: DFS

Bài 1 sử dụng Stack để duyệt các state của trò chơi bao gôm địa điểm của pacman và các hướng đã di chuyển trước đó.

## Bài 2: BFS

Bài 2 sử dụng Queue để duyệt các state của trò chơi bao gồm địa điểm của pacman và các hướng đã di chuyển trước đó.

## Bài 3: UCS

Bài 3 sử dụng Prioriry Queue để duyệt các state của trò chơi gồm địa điểm của pacman và các hướng đã di chuyển trước đó với trọng số ưu tiên là khoảng cách cạnh từ điểm gốc đến điểm đang xét.

## Bài 4: A* Seach

Bài 4 sử dụng Prority Queue để duyệt các state của trò chơi gồm địa điểm của pacman và các hướng đã di chuyển trước đó với trọng số ưu tiên là khoảnh cách cạnh từ điểm đầu đến điểm đang xét cộng với khoảnh cách manhattan từ điểm đang xét đến điểm đích.

## Bài 5: Corners Problem

Ta quy định đích đến của bài toán là phải duyệt qua đủ 4 corners.
Các successors cũng phải trả về các state không phải tường và cập nhật danh sách corners chưa đi được từ các state liền kề state ban đầu

## Bài 6: Corners Heuristic

Ta sử dụng thuật toán như sau: Từ điểm bắt đầu tính khoảng cách manhattan đến corner gần nhất xong tiếp tục tìm corners gần nhất với corner đầu tiên công khoảng cách manhattan vào,... cứ làm như vậy đến khi đi tất cả các corners.

## Bài 7: Food Heuristic

Ta sử dụng Heuristics xong: Tính giá trị lớn nhất về khoảnh cách bfs trong các corners.

## Bài 8: Suboptimal Search

Ta sử dụng thuật toán tìm corners gần nhất rồi đi theo.
