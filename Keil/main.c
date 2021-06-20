#include <reg52.h>
#define uint unsigned int   //16bit
#define uchar unsigned char  // 8bit
#define ADCData P2


sbit OE  = P1^0;
sbit EOC = P1^1;
sbit ST  = P1^2;
sbit CLK = P1^3;

sbit Chanel0 = P0^0;
sbit Chanel1 = P0^1;
sbit Chanel2 = P0^2;
sbit Chanel3 = P0^3;

uchar volData[16];

void DelayMS(uint ms)
{
 	uchar i;
	while(ms--)
	{
	 	for(i=0;i<120;i++);
	}
}

uchar GetData(void)
{
	uchar adcData;
	ST = 0;
	ST = 1;
	ST = 0;
	while(EOC == 0);
	OE = 1;
	DelayMS(2);
	adcData = ADCData;
	OE = 0;
	return adcData;
}




void GetDataLoop()
{
	uchar i;
	for (i=0;i<16;i++){
		Chanel0 = i&1;
		Chanel1 = (i>>1)&1;
		Chanel2 = (i>>2)&1;
		Chanel3 = (i>>3)&1;
//		Chanel0 = 1;
//		Chanel1 = 0;
//		Chanel2 = 1;
//		Chanel3 = 0;
		DelayMS(30); //��ʱʹ��ѹ�ȶ��ٲɼ�
		volData[i] = GetData();
		DelayMS(2);
	}
}


void putc_to_SerialPort(uchar c)
{
 	SBUF = c;
	while(TI == 0);
	TI = 0;
	DelayMS(2);
}


void send_data(uchar *Data){
	uchar i;
	for(i=0;i<16;i++){
		putc_to_SerialPort(Data[i]);
	}
}


void puts_to_SerialPort(uchar *s)
{
 	while(*s != '\0')
	{
	 	putc_to_SerialPort(*s);
		s++;
	}
}


void Init()
{
	TMOD = 0x22; //1-���ڣ�0-ģ��ʱ��
	TH0 = 0x14;
	TL0 = 0x00;
	ET0 = 1;
	TR0 = 1; //��ʱ��0��ʼ����
	IT0 = 1; //��ʱ��0�жϿ���
	
	SCON=0X50; //10λUART����ģʽ
	PCON = 0X00; //�����ʲ��ӱ�
	TH1 = 0xfd; //������9600
	TL1 = 0xfd;
	ES=0; //�رմ����ж�
	EA=1; //����ȫ���ж�
	IP = 0x01;
	TI = 0;
	TR1=1; //��ʱ��1��ʼ����
	
}

void main()
{
	uchar i;
 	Init();
	P1 = 0x0f;	
	i=0;
	while(1)
	{
//		puts_to_SerialPort("\r\n");
		GetDataLoop();
		putc_to_SerialPort(0x00); //���Ϳ�ʼ��־
		send_data(volData);
		putc_to_SerialPort(0xff); //���ͽ�����־
		puts_to_SerialPort("\r\n");//���ͽ�����־
//		puts_to_SerialPort("next\r\n");
		DelayMS(500);
		
	}
}


void Timer0_INT() interrupt 1
{
 	CLK = !CLK;
}

//void serial() interrupt 4
//{
//	if(RI){
//		RI = 0;
//	}

//}