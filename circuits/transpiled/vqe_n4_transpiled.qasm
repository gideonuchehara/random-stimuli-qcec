OPENQASM 2.0;
include "qelib1.inc";
qreg q[4];
creg meas[4];
sx q[0];
rz(-1.2531341) q[0];
sx q[0];
rz(-0.52639697) q[0];
sx q[1];
rz(-0.91711704) q[1];
sx q[1];
rz(-2.4745097) q[1];
cx q[0],q[1];
sx q[0];
rz(-2.1857875) q[0];
sx q[0];
rz(-1.2194001) q[0];
sx q[2];
rz(-3.0769246) q[2];
sx q[2];
rz(-2.5703727) q[2];
cx q[1],q[2];
sx q[1];
rz(-1.4930217) q[1];
sx q[1];
rz(-2.7033598) q[1];
cx q[0],q[1];
sx q[0];
rz(-1.7088065) q[0];
sx q[0];
rz(-1.2804674) q[0];
sx q[3];
rz(-0.094530987) q[3];
sx q[3];
rz(-2.5654104) q[3];
cx q[2],q[3];
sx q[2];
rz(-1.7845974) q[2];
sx q[2];
rz(-2.2237932) q[2];
cx q[1],q[2];
sx q[1];
rz(-0.67488962) q[1];
sx q[1];
rz(-2.9956644) q[1];
cx q[0],q[1];
sx q[0];
rz(-2.937227) q[0];
sx q[0];
rz(-2.1846203) q[0];
sx q[3];
rz(-2.2266693) q[3];
sx q[3];
rz(-1.990633) q[3];
cx q[2],q[3];
sx q[2];
rz(-2.514299) q[2];
sx q[2];
rz(-1.2329342) q[2];
cx q[1],q[2];
sx q[1];
rz(-0.16058082) q[1];
sx q[1];
rz(-2.8347467) q[1];
sx q[3];
rz(-1.5260775) q[3];
sx q[3];
rz(-2.6058753) q[3];
cx q[2],q[3];
sx q[2];
rz(-0.10797015) q[2];
sx q[2];
rz(-0.9920112) q[2];
sx q[3];
rz(-0.60193748) q[3];
sx q[3];
rz(-1.7588128) q[3];
barrier q[0],q[1],q[2],q[3];
measure q[0] -> meas[0];
measure q[1] -> meas[1];
measure q[2] -> meas[2];
measure q[3] -> meas[3];
