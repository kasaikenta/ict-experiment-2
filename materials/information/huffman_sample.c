#include <stdio.h>
#include <string.h>
#include <math.h>

#define CODE_SIZE 128
#define MAX_NODES 256
#define BUFFER_SIZE 1024
#define STRING_SIZE 1024

//自己参照構造体（木構造を作成する）
typedef struct node_t {
  struct node_t *left, *right; //左右の子
  double prob; // 節点の確率
  int symbol; //記号の番号
  int leaf; //葉かどうかのフラグ
} *node; //node_tのポインタをnodeと名付ける
 
//node_t型のpoolをMAX_NODES個作製して初期化。符号の木の節点数が最大MAX_NODES
struct node_t pool[MAX_NODES] = {{0}};
node qqq[MAX_NODES - 1], *q = qqq - 1; //ヒープを実現する配列
int n_nodes = 0; //ハフマン木の節点数
int qend = 1; //ヒープの節点数
char *code[CODE_SIZE] = {0}; //符号語の集合
char buf[BUFFER_SIZE]; //符号語の書き込みに利用する記憶領域
 
node new_node(double prob, int symbol, int leaf, node a, node b)
{
  node n = pool + n_nodes++; //poolから一つ節点を新規割当
  //葉であればnを葉にするための処理を行う
  if (leaf == 1) {
    // ???
  }
  else {
    // ???
  }
  return n;
}
 
void qinsert(node n)
{
  int j, i = qend++;
  while ((j = i / 2)) { //最初はwhile(0)で実行されず
    // ???
  }
  q[i] = n; // 検索した位置にnを追加
}

node qremove()
{
  int i, l;
  node n = q[i = 1]; //根の取り出し
 
  if (qend < 2) return 0;
  qend--;
  while ((l = i * 2) < qend) { //現在の節点の左側の子をlで指定する
    // ???
  }
  // ???
  return n;
}
 
void build_code(node n, char *c, int len)
{
  static char *out = buf;

  //葉にたどり着いたらその葉が表す記号の符号語をcodeに保存する
  if (n->leaf == 1) {
    // ???
  }
  // ???
}

//ハフマン木の作成 
void init(int asize, double *prob)
{
  int i;
  char c[MAX_NODES]; //1つの符号語の長さは節点数の最大値としておく  
  //節点を新規に作成しながら確率の低い順にヒープを作る
  for (i = 0; i < asize; i++)
    qinsert(new_node(prob[i], i, 1, 0, 0));

  /* 以下の動作
   * （１）qremoveで最も頻度の低い二つのノードを選びキューから取り出す
   * （２）new_nodeでそれらを合算した新たなノードを作成する
   * （３）新たなノードの左右の子ノードには合算するノードを割り振る
   * （４）qinsertで新たに作成したノードをキューに入れる
   */

  // ???

  build_code(q[1], c, 0);
}

void encode(char *s, int *isymb, char *out)
{
  while (*s) {
    // ???
  }
}

void decode( char *symb, char *c, node t)
{
  node n = t;
  while (*c) {
    // ???
  } 
}

double H(int asize, double *prob) {
  double h = 0;
  // ???
  return h;
}

double alength(int asize, double *prob) {
  double al = 0;
  // ???
  return al;
} 

int main(void)
{
  int asize;
  printf("alphabet size> ");
  scanf("%d", &asize);
  double prob[asize];
  char symb[asize];
  for(int i = 0; i < asize; i++) {
    printf("symbol_%d> ", i + 1);
    scanf("%s", &symb[i]);
    printf("p_%d> ", i + 1);
    scanf("%lf", &prob[i]);
  }

  //ハフマン木の作成
  init(asize, prob);

  //codewords
  for (int i = 0; i < asize; i++)
    if(code[i]) printf("cw for %c: %s\n", symb[i], code[i]);

  //entropy
  printf("entropy: %lf\n", H(asize, prob));

  //average length
  printf("average length: %lf\n", alength(asize, prob));

  //記号の逆引き配列を作成すると便利
  int isymb[128] = {0}; //ASCII文字を仮定する
  for(int i = 0; i < asize; i++) isymb[symb[i]] = i;

  //encoded
  char ss[STRING_SIZE] = {0};
  printf("symbols> ");
  scanf("%s", ss);
  char out[STRING_SIZE] = {0};
  encode(ss, isymb, out);
  printf("encoded: %s\n", out);

  //decoded
  char cdws[STRING_SIZE] = {0};
  printf("codewords> ");
  scanf("%s", cdws);
  printf("decoded: ");
  decode(symb, cdws, q[1]);
 
  return 0;
}
