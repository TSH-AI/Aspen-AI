using Infragistics.Win;
using Infragistics.Win.FormattedLinkLabel;
using Infragistics.Win.UltraWinGrid;
using Micromind.ClientLibraries;
using Micromind.ClientUI.Libraries;
using Micromind.ClientUI.Properties;
using Micromind.ClientUI.WindowsForms.DataEntries.Others;
using Micromind.Common;
using Micromind.Common.Data;
using Micromind.Common.Interfaces;
using Micromind.DataControls;
using Micromind.UISupport;
using System;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Globalization;
using System.Windows.Forms;

namespace Micromind.ClientUI.WindowsForms.DataEntries.Accounts
{
	public class TRApplicationForm : Form, IForm, IWorkFlowForm
	{
		private bool allowEdit = true;

		private TRApplicationData currentData;

		private const string TABLENAME_CONST = "TR_Application";

		private const string IDFIELD_CONST = "VoucherID";

		private bool isNewRecord = true;

		private bool isCostCenterMandatory = CompanyPreferences.IsCostCenterMandatory;

		private bool allowMultiTemplate;

		private decimal TotBalance;

		private decimal TotDue;

		private int totPC;

		private int totQC;

		private decimal balance;

		private decimal dueBalance;

		private decimal purchaseclaimamt;

		private decimal qualityclaimamt;

		private decimal AvailableBal;

		private string currentCustomerID;

		private string requestSysDocID = "";

		private bool isDataLoading;

		private ScreenAccessRight screenRight;

		private bool AllowEditTransaction;

		private bool AllowEditTransDiffLocation;

		private bool isVoid;

		private IContainer components;

		private Panel panelButtons;

		private Line linePanelDown;

		private XPButton xpButton1;

		private XPButton buttonSave;

		private FormManager formManager;

		private TextBox textBoxNote;

		private Label label3;

		private XPButton buttonDelete;

		private XPButton buttonNew;

		private XPButton buttonVoid;

		private ContextMenuStrip contextMenuStrip1;

		private ToolStripMenuItem availableQuantityToolStripMenuItem;

		private ToolStripMenuItem salesStatisticsToolStripMenuItem;

		private ToolStripMenuItem itemPicToolStripMenuItem;

		private ToolStripMenuItem itemDetailsToolStripMenuItem;

		private ToolStripSeparator toolStripSeparator3;

		private ToolStripMenuItem removeRowToolStripMenuItem;

		private ComboBox comboBoxReason;

		private Label label2;

		private PaymentTermComboBox comboBoxPOTerm;

		private Panel panelTR;

		private Label label18;

		private Label label17;

		private Label label16;

		private Label label15;

		private Label label14;

		private Label labelInvnos;

		private TextBox textBoxAuthorizedby;

		private TextBox textBoxInvoiceNo;

		private NumberTextBox textBoxNoofPLs;

		private NumberTextBox textBoxNoofBOLs;

		private NumberTextBox textBoxNoofInvoices;

		private TextBox textBoxNoofGoods;

		private Panel panelDetails;

		private XPButton buttonSelectRequest;

		private UltraFormattedLinkLabel ultraFormattedLinkLabel1;

		private TextBox textBoxRequest;

		private UltraFormattedLinkLabel ultraFormattedLinkLabel5;

		private vendorsFlatComboBox comboBoxVendor;

		private MMLabel mmLabel1;

		private Label label1;

		private CurrencySelector currencySelector;

		private TextBox textBoxDescription;

		private TextBox textBoxTRNote;

		private Label label4;

		private UltraFormattedLinkLabel labelCurrency;

		private UltraFormattedLinkLabel ultraFormattedLinkLabel2;

		private UltraFormattedLinkLabel ultraFormattedLinkLabel3;

		private flatDatePicker dateTimePickerDate;

		private TextBox textBoxVoucherNumber;

		private CostCenterComboBox comboBoxCostCenter;

		private TextBox textBoxPayeeName;

		private UltraFormattedLinkLabel ultraFormattedLinkLabel6;

		private SysDocComboBox comboBoxSysDoc;

		private UltraFormattedLinkLabel ultraFormattedLinkLabel8;

		private XPButton buttonSelectInvoice;

		private UltraFormattedLinkLabel ultraFormattedLinkLabel4;

		private NumericUpDown numericUpDownTenorDay;

		private TextBox textBoxRegBalance;

		private Label label19;

		private flatDatePicker datePickerDueDate;

		private TextBox textBoxRef1;

		private Label labelAmountBase;

		private AmountTextBox textBoxAmount;

		private Label label21;

		private TextBox textBoxAmountBase;

		private Label label22;

		private BankFacilityComboBox comboBoxFacility;

		private MMLabel mmLabel7;

		private TextBox textBoxFacilityName;

		private ToolStripButton toolStripButtonFirst;

		private ToolStripButton toolStripButtonPrevious;

		private ToolStripButton toolStripButtonNext;

		private ToolStripButton toolStripButtonLast;

		private ToolStripSeparator toolStripSeparator1;

		private ToolStripButton toolStripButtonOpenList;

		private ToolStripSeparator toolStripSeparator5;

		private ToolStripTextBox toolStripTextBoxFind;

		private ToolStripButton toolStripButtonFind;

		private ToolStripSeparator toolStripSeparator2;

		private ToolStripButton toolStripButtonPreview;

		private ToolStripButton toolStripButtonPrint;

		private ToolStripSeparator toolStripSeparator7;

		private ToolStripButton toolStripButtonAttach;

		private ToolStripSeparator toolStripSeparator4;

		private ToolStripDropDownButton toolStripDropDownButton1;

		private ToolStripMenuItem duplicateToolStripMenuItem;

		private ToolStripSeparator toolStripSeparator6;

		private ToolStripMenuItem saveDraftToolStripMenuItem;

		private ToolStripMenuItem loadDraftToolStripMenuItem;

		private ToolStripButton toolStripButtonApproval;

		private ToolStripLabel toolStripLabelApproval;

		private ToolStripSeparator toolStripSeparatorApproval;

		private ToolStripButton toolStripButtonPrintTemplate;

		private ToolStripButton toolStripButtonInformation;

		private ToolStrip toolStrip1;

		private Panel panel1;

		private Panel panelPO;

		private TextBox dateTimePickerETA;

		private Label label13;

		private TextBox textBoxPOSysDocID;

		private XPButton buttonSelectPO;

		private TextBox textBoxPOVoucherID;

		private Label label9;

		private TextBox textBoxPOTerm;

		private Label label8;

		private AmountTextBox textBoxPOBalance;

		private Label label7;

		private AmountTextBox textBoxPOPaid;

		private Label label6;

		private AmountTextBox textBoxPOAmount;

		private Label label5;

		private PaymentTermComboBox paymentTermComboBox1;

		private Label labelVoided;

		private Label label10;

		private MMLabel mmLabel4;

		private AmountTextBox textBoxTotalDue;

		private MMLabel labelVendorBalance;

		private AmountTextBox textBoxTotalBalance;

		private TextBox textBoxTerm;

		private Label textBoxTotalQualityClaim;

		private Label textBoxTotalPurchaseClaim;

		private BALinkLabel linklabelPC;

		private BALinkLabel linklabelQC;

		private MMLabel mmLabel6;

		private MMLabel mmLabel3;

		private ToolStripButton toolStripButtonMultiPreview;

		private PaymentTermComboBox comboBoxVendorTerm;

		public ScreenAreas ScreenArea => ScreenAreas.Sales;

		public int ScreenID => 2011;

		public ScreenTypes ScreenType => ScreenTypes.Transaction;

		public string CurrentCustomerID
		{
			get
			{
				return currentCustomerID;
			}
			set
			{
				currentCustomerID = value;
			}
		}

		private string SystemDocID => comboBoxSysDoc.SelectedID;

		private bool IsDirty
		{
			get
			{
				if (IsVoid)
				{
					return false;
				}
				return formManager.GetDirtyStatus();
			}
		}

		private bool IsNewRecord
		{
			get
			{
				return isNewRecord;
			}
			set
			{
				isNewRecord = value;
				bool enabled;
				if (value)
				{
					buttonNew.Text = UIMessages.ClearButtonText;
					XPButton xPButton = buttonDelete;
					enabled = (buttonVoid.Enabled = false);
					xPButton.Enabled = enabled;
					textBoxVoucherNumber.Enabled = true;
					SysDocComboBox sysDocComboBox = comboBoxSysDoc;
					enabled = (buttonSelectInvoice.Enabled = true);
					sysDocComboBox.Enabled = enabled;
				}
				else
				{
					buttonNew.Text = UIMessages.NewButtonText;
					XPButton xPButton2 = buttonDelete;
					enabled = (buttonVoid.Enabled = true);
					xPButton2.Enabled = enabled;
					textBoxVoucherNumber.Enabled = false;
					comboBoxSysDoc.Enabled = false;
					buttonSelectInvoice.Enabled = false;
				}
				buttonSelectRequest.Enabled = value;
				comboBoxSysDoc.Enabled = value;
				toolStripButtonAttach.Enabled = !value;
				if (!screenRight.New && isNewRecord)
				{
					buttonSave.Enabled = false;
					buttonVoid.Enabled = false;
				}
				else if (!screenRight.Edit && !isNewRecord)
				{
					buttonSave.Enabled = false;
					buttonVoid.Enabled = false;
				}
				else
				{
					buttonSave.Enabled = true;
				}
				if (!screenRight.Delete)
				{
					buttonDelete.Enabled = false;
				}
				ToolStripButton toolStripButton = toolStripButtonPrint;
				enabled = (toolStripButtonPreview.Enabled = !isNewRecord);
				toolStripButton.Enabled = enabled;
			}
		}

		private bool IsVoid
		{
			get
			{
				return isVoid;
			}
			set
			{
				if (isVoid != value && isVoid != value)
				{
					isVoid = value;
					buttonSave.Enabled = !value;
					panelDetails.Enabled = !value;
					labelVoided.Visible = value;
					if (value)
					{
						buttonVoid.Text = UIMessages.Unvoid;
					}
					else
					{
						buttonVoid.Text = UIMessages.Void;
					}
				}
			}
		}

		public TRApplicationForm()
		{
			InitializeComponent();
			AddEvents();
			comboBoxFacility.FilterFacilityType = BankFacilityTypes.TR;
			comboBoxReason.SelectedIndex = 0;
			comboBoxReason.SelectedIndexChanged += comboBoxReason_SelectedIndexChanged;
			comboBoxFacility.SelectedIndexChanged += comboBoxBank_SelectedIndexChanged;
			comboBoxVendor.SelectedIndexChanged += comboBoxVendor_SelectedIndexChanged;
			currencySelector.CurrencyRateChanged += currencySelector_CurrencyRateChanged;
			currencySelector.SelectedIndexChanged += currencySelector_SelectedIndexChanged;
			comboBoxType_SelectedIndexChanged(null, null);
			comboBoxSysDoc.SelectedIndexChanged += comboBoxSysDoc_SelectedIndexChanged;
		}

		private void currencySelector_SelectedIndexChanged(object sender, EventArgs e)
		{
			CalculateBaseAmount();
		}

		private void currencySelector_CurrencyRateChanged(object sender, EventArgs e)
		{
			CalculateBaseAmount();
		}

		private void comboBoxCurrency_SelectedIndexChanged(object sender, EventArgs e)
		{
			CalculateBaseAmount();
		}

		private void textBoxAmount_TextChanged(object sender, EventArgs e)
		{
			CalculateBaseAmount();
		}

		private void CalculateBaseAmount()
		{
			if (currencySelector.IsBaseCurrency)
			{
				textBoxAmountBase.Text = textBoxAmount.Text;
				return;
			}
			decimal result = default(decimal);
			decimal.TryParse(textBoxAmount.Text, out result);
			textBoxAmountBase.Text = currencySelector.GetBaseEquivalant(result).ToString(Format.TotalAmountFormat);
		}

		private void comboBoxVendor_SelectedIndexChanged(object sender, EventArgs e)
		{
			try
			{
				textBoxAmount.Clear();
				textBoxPayeeName.Text = comboBoxVendor.SelectedName;
				if (comboBoxVendor.AllowOAP)
				{
					textBoxAmount.ReadOnly = false;
				}
				else
				{
					textBoxAmount.ReadOnly = true;
				}
				if (textBoxAmount.Tag != null)
				{
					textBoxAmount.Tag = null;
					textBoxAmount.Clear();
				}
				if (string.IsNullOrEmpty(comboBoxVendor.SelectedID))
				{
					goto IL_00d1;
				}
				bool result = false;
				bool.TryParse(Factory.DatabaseSystem.GetFieldValue("Vendor", "IsHoldForPayment", "VendorID", comboBoxVendor.SelectedID).ToString(), out result);
				if (!result || !IsNewRecord)
				{
					goto IL_00d1;
				}
				ErrorHelper.WarningMessage("This vendor is on hold status and does not allow transaction.");
				goto end_IL_0000;
				IL_00d1:
				LoadVendorDetails();
				end_IL_0000:;
			}
			catch (Exception e2)
			{
				ErrorHelper.ProcessError(e2);
			}
		}

		public void LoadVendorDetails()
		{
			string text = "";
			string text2 = "";
			string selectedID = comboBoxVendor.SelectedID;
			object fieldValue = Factory.DatabaseSystem.GetFieldValue("Vendor", "CurrencyID", "VendorID", selectedID);
			object fieldValue2 = Factory.DatabaseSystem.GetFieldValue("Vendor", "PaymentTermID", "VendorID", selectedID);
			DataSet vendorDueBalanceSummary = Factory.VendorSystem.GetVendorDueBalanceSummary(selectedID, fieldValue.ToString(), dateTimePickerDate.Value);
			if (vendorDueBalanceSummary != null && vendorDueBalanceSummary.Tables[0].Rows.Count > 0)
			{
				balance = decimal.Parse(vendorDueBalanceSummary.Tables[0].Rows[0]["Balance"].ToString());
				dueBalance = decimal.Parse(vendorDueBalanceSummary.Tables[0].Rows[0]["BalanceDue"].ToString());
				purchaseclaimamt = decimal.Parse(vendorDueBalanceSummary.Tables[0].Rows[0]["Purchaseclaimamt"].ToString());
				qualityclaimamt = decimal.Parse(vendorDueBalanceSummary.Tables[0].Rows[0]["Qualityclaimamt"].ToString());
				text = vendorDueBalanceSummary.Tables[0].Rows[0]["PCCount"].ToString();
				text2 = vendorDueBalanceSummary.Tables[0].Rows[0]["QCCount"].ToString();
			}
			TotBalance = balance;
			TotDue = dueBalance;
			if (isNewRecord)
			{
				textBoxTotalBalance.Text = balance.ToString(Format.TotalAmountFormat);
			}
			textBoxTotalDue.Text = dueBalance.ToString(Format.TotalAmountFormat);
			textBoxTotalQualityClaim.Text = qualityclaimamt.ToString(Format.TotalAmountFormat);
			textBoxTotalPurchaseClaim.Text = purchaseclaimamt.ToString(Format.TotalAmountFormat);
			totPC = int.Parse(text);
			totQC = int.Parse(text2);
			linklabelQC.Text = "(" + text2 + ")";
			linklabelPC.Text = "(" + text + ")";
			labelVendorBalance.Text = "Balance: (" + fieldValue + ")";
			comboBoxVendorTerm.SelectedID = fieldValue2.ToString();
		}

		private void comboBoxBank_SelectedIndexChanged(object sender, EventArgs e)
		{
			try
			{
				AvailableBal = default(decimal);
			}
			catch (Exception e2)
			{
				ErrorHelper.ProcessError(e2);
			}
		}

		private void comboBoxReason_SelectedIndexChanged(object sender, EventArgs e)
		{
			panelPO.Visible = (comboBoxReason.SelectedIndex == 0);
		}

		private void comboBoxType_SelectedIndexChanged(object sender, EventArgs e)
		{
		}

		private void AddEvents()
		{
			base.Load += Form_Load;
			comboBoxSysDoc.SelectedIndexChanged += comboBoxSysDoc_SelectedIndexChanged;
			base.FormClosing += Form_FormClosing;
			base.KeyDown += TRApplicationForm_KeyDown;
		}

		private void TRApplicationForm_KeyDown(object sender, KeyEventArgs e)
		{
			if (e.Control && e.KeyCode == Keys.P && !IsNewRecord)
			{
				Print(isPrint: true, showPrintDialog: true, saveChanges: true);
			}
		}

		private void comboBoxGridItem_VisibleChanged(object sender, EventArgs e)
		{
		}

		private void comboBoxSysDoc_SelectedIndexChanged(object sender, EventArgs e)
		{
			if (!isDataLoading)
			{
				if (isNewRecord)
				{
					textBoxVoucherNumber.Text = GetNextVoucherNumber();
				}
				formManager.SetControlDirtyStatus(textBoxVoucherNumber, textBoxVoucherNumber.Text);
				allowMultiTemplate = false;
				object fieldValue = Factory.DatabaseSystem.GetFieldValue("System_Document", "AllowMultiTemplate", "SysDocID", comboBoxSysDoc.SelectedID);
				if (fieldValue != null && fieldValue.ToString() != "")
				{
					allowMultiTemplate = bool.Parse(fieldValue.ToString());
				}
				if (allowMultiTemplate)
				{
					toolStripButtonMultiPreview.Visible = true;
				}
				else
				{
					toolStripButtonMultiPreview.Visible = false;
				}
			}
		}

		private void dataGrid_BeforeCellUpdate(object sender, BeforeCellUpdateEventArgs e)
		{
		}

		private bool GetData()
		{
			try
			{
				if (currentData == null || isNewRecord)
				{
					currentData = new TRApplicationData();
				}
				DataRow dataRow = (!isNewRecord) ? currentData.TRApplicationTable.Rows[0] : currentData.TRApplicationTable.NewRow();
				dataRow["SysDocType"] = (byte)248;
				if (textBoxDescription.Text.Trim() != "")
				{
					dataRow["Description"] = textBoxDescription.Text;
				}
				else
				{
					dataRow["Description"] = textBoxTRNote.Text;
				}
				dataRow["CostCenterID"] = comboBoxCostCenter.SelectedID;
				dataRow["TransactionDate"] = dateTimePickerDate.Value;
				dataRow["SysDocID"] = comboBoxSysDoc.SelectedID;
				dataRow["VoucherID"] = textBoxVoucherNumber.Text;
				dataRow["Reference"] = textBoxRef1.Text;
				if (textBoxRequest.Text != "")
				{
					dataRow["RequestSysDocID"] = requestSysDocID;
					dataRow["RequestVoucherID"] = textBoxRequest.Text;
				}
				else
				{
					dataRow["RequestSysDocID"] = DBNull.Value;
					dataRow["RequestVoucherID"] = DBNull.Value;
				}
				dataRow["BankFacilityID"] = comboBoxFacility.SelectedID;
				dataRow["Reference"] = textBoxRef1.Text;
				dataRow["PayeeType"] = "V";
				dataRow["PayeeID"] = comboBoxVendor.SelectedID;
				dataRow["DueDate"] = datePickerDueDate.Value;
				if (currencySelector.SelectedID != "" && currencySelector.SelectedID != Global.BaseCurrencyID)
				{
					dataRow["CurrencyID"] = currencySelector.SelectedID;
					dataRow["CurrencyRate"] = currencySelector.Rate;
					dataRow["AmountFC"] = textBoxAmount.Text;
				}
				else
				{
					dataRow["CurrencyID"] = DBNull.Value;
					dataRow["CurrencyRate"] = 1;
					dataRow["Amount"] = textBoxAmount.Text;
				}
				if (textBoxPOVoucherID.Text != "")
				{
					dataRow["POSysDocID"] = textBoxPOSysDocID.Text;
					dataRow["POVoucherID"] = textBoxPOVoucherID.Text;
				}
				else
				{
					dataRow["POSysDocID"] = DBNull.Value;
					dataRow["POVoucherID"] = DBNull.Value;
				}
				dataRow["InvoiceNos"] = textBoxInvoiceNo.Text;
				dataRow["Authorizedby"] = textBoxAuthorizedby.Text;
				dataRow["NoofInvoices"] = textBoxNoofInvoices.Text;
				dataRow["NoofPL"] = textBoxNoofPLs.Text;
				dataRow["NoofBOL"] = textBoxNoofBOLs.Text;
				dataRow["NoofGoods"] = textBoxNoofGoods.Text;
				dataRow["Note"] = textBoxNote.Text;
				dataRow.EndEdit();
				if (IsNewRecord)
				{
					currentData.TRApplicationTable.Rows.Add(dataRow);
				}
				if (textBoxAmount.Tag != null)
				{
					DataSet dataSet = textBoxAmount.Tag as DataSet;
					dataSet = dataSet.Copy();
					if (currentData.Tables.Contains("AP_Payment_Advice"))
					{
						currentData.Tables.Remove("AP_Payment_Advice");
					}
					string a = Global.BaseCurrencyID;
					foreach (DataRow row in dataSet.Tables["AP_Payment_Advice"].Rows)
					{
						if (!row["CurrencyID"].IsDBNullOrEmpty())
						{
							a = row["CurrencyID"].ToString();
						}
						row["PaymentSysDocID"] = comboBoxSysDoc.SelectedID;
						row["PaymentVoucherID"] = textBoxVoucherNumber.Text;
						row["AllocationDate"] = dateTimePickerDate.Value;
						row["IsDraft"] = true;
					}
					if (a != currencySelector.SelectedID)
					{
						ErrorHelper.WarningMessage("Currency should not change after selecting invoices.");
						return false;
					}
					currentData.Merge(dataSet.Tables["AP_Payment_Advice"]);
				}
				return true;
			}
			catch (Exception e)
			{
				ErrorHelper.ProcessError(e);
				return false;
			}
		}

		private void buttonSave_Click(object sender, EventArgs e)
		{
			SaveData();
		}

		public void LoadData(string voucherID)
		{
			try
			{
				if (!base.IsDisposed && !(voucherID.Trim() == "") && CanClose())
				{
					currentData = Factory.TRApplicationSystem.GetTRApplicationByID(SystemDocID, voucherID);
					if (currentData != null)
					{
						FillData();
						IsNewRecord = false;
						formManager.ResetDirty();
					}
				}
			}
			catch (Exception e)
			{
				ErrorHelper.ProcessError(e);
				ClearForm();
			}
		}

		private void FillData()
		{
			try
			{
				isDataLoading = true;
				if (currentData != null && currentData.Tables.Count != 0 && currentData.Tables["TR_Application"].Rows.Count != 0)
				{
					DataRow dataRow = currentData.Tables["TR_Application"].Rows[0];
					dateTimePickerDate.Value = DateTime.Parse(dataRow["TransactionDate"].ToString());
					textBoxVoucherNumber.Text = dataRow["VoucherID"].ToString();
					textBoxRef1.Text = dataRow["Reference"].ToString();
					comboBoxCostCenter.SelectedID = dataRow["CostCenterID"].ToString();
					textBoxTRNote.Text = dataRow["Description"].ToString();
					comboBoxVendor.SelectedID = dataRow["PayeeID"].ToString();
					requestSysDocID = dataRow["RequestSysDocID"].ToString();
					textBoxRequest.Text = dataRow["RequestVoucherID"].ToString();
					if (textBoxRequest.Text != "")
					{
						comboBoxVendor.Enabled = false;
						comboBoxFacility.Enabled = false;
					}
					comboBoxFacility.SelectedID = dataRow["BankFacilityID"].ToString();
					if (dataRow["IsVoid"] != DBNull.Value)
					{
						IsVoid = bool.Parse(dataRow["IsVoid"].ToString());
					}
					else
					{
						IsVoid = false;
					}
					if (dataRow["AmountFC"] != DBNull.Value)
					{
						textBoxAmount.Text = Math.Round(decimal.Parse(dataRow["AmountFC"].ToString()), Global.CurDecimalPoints).ToString(Format.TotalAmountFormat);
					}
					else if (dataRow["Amount"] != DBNull.Value)
					{
						textBoxAmount.Text = Math.Round(decimal.Parse(dataRow["Amount"].ToString()), Global.CurDecimalPoints).ToString(Format.TotalAmountFormat);
					}
					else
					{
						textBoxAmount.Text = 0.ToString(Format.TotalAmountFormat);
					}
					if (dataRow["CurrencyID"] != DBNull.Value)
					{
						currencySelector.SelectedID = dataRow["CurrencyID"].ToString();
						currencySelector.Rate = decimal.Parse(dataRow["CurrencyRate"].ToString());
					}
					else
					{
						currencySelector.SelectedID = "";
						currencySelector.Rate = 1m;
					}
					CalculateBaseAmount();
					datePickerDueDate.Value = DateTime.Parse(dataRow["DueDate"].ToString());
					TimeSpan timeSpan = dateTimePickerDate.Value - datePickerDueDate.Value;
					numericUpDownTenorDay.Value = Math.Abs(timeSpan.Days);
					textBoxPOSysDocID.Text = dataRow["POSysDocID"].ToString();
					textBoxPOVoucherID.Text = dataRow["POVoucherID"].ToString();
					textBoxInvoiceNo.Text = dataRow["InvoiceNos"].ToString();
					textBoxAuthorizedby.Text = dataRow["Authorizedby"].ToString();
					textBoxNoofInvoices.Text = dataRow["NoofInvoices"].ToString();
					textBoxNoofPLs.Text = dataRow["NoofPL"].ToString();
					textBoxNoofBOLs.Text = dataRow["NoofBOL"].ToString();
					textBoxNoofGoods.Text = dataRow["NoofGoods"].ToString();
					if (dataRow["IsVoid"] != DBNull.Value)
					{
						IsVoid = bool.Parse(dataRow["IsVoid"].ToString());
					}
					else
					{
						IsVoid = false;
					}
					FillPOData();
					if (currentData.Tables["AP_Payment_Advice"] != null)
					{
						textBoxAmount.Tag = currentData;
						textBoxAmount.ReadOnly = true;
					}
				}
			}
			catch
			{
				throw;
			}
			finally
			{
				isDataLoading = false;
			}
		}

		private bool SaveData()
		{
			if (!IsDirty)
			{
				if (!IsNewRecord)
				{
					IsNewRecord = true;
					ClearForm();
				}
				return true;
			}
			if (!IsNewRecord)
			{
				switch (ErrorHelper.QuestionMessageYesNoCancel(UIMessages.DoYouWantToSave))
				{
				case DialogResult.No:
					return true;
				case DialogResult.Cancel:
					return false;
				}
			}
			return SaveData(clearAfter: true);
		}

		private bool SaveData(bool clearAfter)
		{
			if (!allowEdit)
			{
				ErrorHelper.InformationMessage(Application.ProductName, "You cannot edit this transfer transaction because it is already accepted or rejected.", "Document is in use.");
				return false;
			}
			if (!ValidateData())
			{
				return false;
			}
			if (!GetData())
			{
				return false;
			}
			bool flag = false;
			try
			{
				bool flag2 = false;
				flag2 = ((!isNewRecord) ? Factory.TRApplicationSystem.UpdateTRApplication(currentData) : Factory.TRApplicationSystem.CreateTRApplication(currentData));
				if (flag2)
				{
					flag = true;
				}
				if (!flag2)
				{
					ErrorHelper.ErrorMessage(UIMessages.UnableToSave);
				}
				else
				{
					bool result = false;
					bool.TryParse(comboBoxSysDoc.GetSelectedCellValue("PrintAfterSave").ToString(), out result);
					if (result)
					{
						Print(isPrint: true, showPrintDialog: true, saveChanges: false);
					}
					if (clearAfter)
					{
						ClearForm();
						IsNewRecord = true;
					}
					else
					{
						formManager.ResetDirty();
					}
				}
				return flag2;
			}
			catch (CompanyException ex)
			{
				if (ex.Number == 1046)
				{
					string nextVoucherNumber = GetNextVoucherNumber();
					if (nextVoucherNumber == textBoxVoucherNumber.Text)
					{
						ErrorHelper.WarningMessage(UIMessages.DocumentNumberInUse);
						return false;
					}
					if (nextVoucherNumber != "")
					{
						textBoxVoucherNumber.Text = nextVoucherNumber;
					}
					formManager.SetControlDirtyStatus(textBoxVoucherNumber, textBoxVoucherNumber.Text);
					return SaveData();
				}
				ErrorHelper.ProcessError(ex);
				return false;
			}
			catch (Exception e)
			{
				ErrorHelper.ProcessError(e);
				return false;
			}
			finally
			{
				if (flag)
				{
					if (clearAfter)
					{
						ClearForm();
						IsNewRecord = true;
					}
					else
					{
						formManager.ResetDirty();
					}
				}
			}
		}

		public void SetApprovalStatus()
		{
			if (IsNewRecord)
			{
				ToolStripButton toolStripButton = toolStripButtonApproval;
				ToolStripLabel toolStripLabel = toolStripLabelApproval;
				bool flag2 = toolStripSeparatorApproval.Visible = false;
				bool visible = toolStripLabel.Visible = flag2;
				toolStripButton.Visible = visible;
			}
			else
			{
				if (currentData == null || currentData.Tables[0].Rows.Count <= 0)
				{
					return;
				}
				DataRow dataRow = currentData.Tables[0].Rows[0];
				bool flag2;
				bool visible;
				if (!dataRow.Table.Columns.Contains("ApprovalStatus") || dataRow["ApprovalStatus"].IsDBNullOrEmpty())
				{
					ToolStripButton toolStripButton2 = toolStripButtonApproval;
					ToolStripLabel toolStripLabel2 = toolStripLabelApproval;
					flag2 = (toolStripSeparatorApproval.Visible = false);
					visible = (toolStripLabel2.Visible = flag2);
					toolStripButton2.Visible = visible;
					return;
				}
				switch (int.Parse(dataRow["ApprovalStatus"].ToString()))
				{
				case 3:
					toolStripButtonApproval.Text = "Rejected";
					toolStripButtonApproval.ForeColor = Color.Red;
					break;
				case 10:
					toolStripButtonApproval.Text = "Approved";
					toolStripButtonApproval.ForeColor = Color.ForestGreen;
					break;
				default:
					toolStripButtonApproval.Text = "Pending";
					toolStripButtonApproval.ForeColor = Color.Orange;
					break;
				}
				ToolStripButton toolStripButton3 = toolStripButtonApproval;
				ToolStripLabel toolStripLabel3 = toolStripLabelApproval;
				flag2 = (toolStripSeparatorApproval.Visible = true);
				visible = (toolStripLabel3.Visible = flag2);
				toolStripButton3.Visible = visible;
			}
		}

		public void ShowForApproval(string sysDocID, string voucherID, int approvalTaskID)
		{
			EditDocument(sysDocID, voucherID);
			panelButtons.Visible = false;
			toolStrip1.Enabled = false;
			formManager.ShowApprovalPanel(approvalTaskID, "TR_Application", "VoucherID");
		}

		private bool ValidateData()
		{
			if (!screenRight.New && isNewRecord)
			{
				ErrorHelper.WarningMessage(UIMessages.NoPermissionNew);
				return false;
			}
			if (!screenRight.Edit && !isNewRecord)
			{
				ErrorHelper.WarningMessage(UIMessages.NoPermissionEdit);
				return false;
			}
			if (!IsNewRecord && !Global.IsUserAdmin && !AllowEditTransaction && Global.CurrentUser != Factory.SystemDocumentSystem.GetTransUserID("TR_Application", "VoucherID", SystemDocID, textBoxVoucherNumber.Text))
			{
				ErrorHelper.WarningMessage("You dont have permission to edit.");
				return false;
			}
			if (!Factory.SystemDocumentSystem.HasuserAccess(comboBoxSysDoc.SelectedID, Global.DefaultLocationID) && !Global.IsUserAdmin && !AllowEditTransDiffLocation)
			{
				ErrorHelper.WarningMessage("You dont have permission to edit (SecurityRoleID:117).");
				return false;
			}
			DateTime t = new DateTime(DateTime.Now.Year, DateTime.Now.Month, DateTime.Now.Day, 23, 59, 59);
			if (isNewRecord && dateTimePickerDate.Value < t && !Security.IsAllowedSecurityRole(GeneralSecurityRoles.EnterBackDatedTransaction))
			{
				ErrorHelper.WarningMessage("You are not allowed to enter back-dated transactions.");
				return false;
			}
			if (isNewRecord && dateTimePickerDate.Value > t && !Security.IsAllowedSecurityRole(GeneralSecurityRoles.FutureDatedTransaction))
			{
				ErrorHelper.WarningMessage("You are not allowed to enter future-dated transactions.");
				return false;
			}
			if (!IsNewRecord && Factory.PaymentRequestSystem.OrderHasShippedQuantity(comboBoxSysDoc.SelectedID, textBoxVoucherNumber.Text))
			{
				ErrorHelper.ErrorMessage("Some items in this order has been already shipped. You are not able to modify.");
				return false;
			}
			if (comboBoxFacility.PayableAccountID == "")
			{
				ErrorHelper.WarningMessage("Payable account is not set for the selected bank facility.");
				return false;
			}
			if (textBoxVoucherNumber.Text.Trim() == "" || comboBoxSysDoc.SelectedID == "")
			{
				ErrorHelper.InformationMessage(UIMessages.EnterRequiredFields);
				return false;
			}
			if (isCostCenterMandatory && comboBoxCostCenter.SelectedID == string.Empty)
			{
				ErrorHelper.InformationMessage("Please select cost center");
				return false;
			}
			if (comboBoxVendor.SelectedID == "")
			{
				ErrorHelper.InformationMessage("Please select a payee.");
				return false;
			}
			if (formManager.IsFieldDirty(textBoxVoucherNumber) && Factory.SystemDocumentSystem.ExistDocumentNumber("TR_Application", "VoucherID", SystemDocID, textBoxVoucherNumber.Text))
			{
				ErrorHelper.WarningMessage(UIMessages.DocumentNumberInUse);
				textBoxVoucherNumber.Focus();
				return false;
			}
			if (!string.IsNullOrEmpty(comboBoxVendor.SelectedID))
			{
				bool result = false;
				bool.TryParse(Factory.DatabaseSystem.GetFieldValue("Vendor", "IsHoldForPayment", "VendorID", comboBoxVendor.SelectedID).ToString(), out result);
				if (result && IsNewRecord)
				{
					ErrorHelper.WarningMessage("This vendor is on hold status and does not allow transaction.");
					return false;
				}
			}
			return true;
		}

		private decimal GetTransactionBalance()
		{
			return 0m;
		}

		private void buttonNew_Click(object sender, EventArgs e)
		{
			if (IsNewRecord)
			{
				ClearForm();
			}
			else if (SaveData())
			{
				ClearForm();
				IsNewRecord = true;
			}
		}

		private void ClearForm()
		{
			try
			{
				allowEdit = true;
				textBoxNote.Clear();
				textBoxRef1.Clear();
				comboBoxVendor.Clear();
				comboBoxFacility.Clear();
				textBoxPOBalance.Text = 0.ToString(Format.TotalAmountFormat);
				textBoxPOAmount.Text = 0.ToString(Format.TotalAmountFormat);
				textBoxPOSysDocID.Clear();
				textBoxPOVoucherID.Clear();
				textBoxPayeeName.Clear();
				textBoxTRNote.Clear();
				textBoxRequest.Clear();
				requestSysDocID = "";
				textBoxAmount.ReadOnly = false;
				textBoxAmount.Tag = null;
				currencySelector.Enabled = true;
				comboBoxVendor.Enabled = true;
				comboBoxFacility.Enabled = true;
				textBoxPOTerm.Clear();
				textBoxRegBalance.Clear();
				textBoxPOPaid.Text = "0.0";
				textBoxDescription.Clear();
				textBoxInvoiceNo.Clear();
				textBoxAuthorizedby.Clear();
				textBoxNoofInvoices.Text = "0";
				textBoxNoofBOLs.Text = "0";
				textBoxNoofGoods.Clear();
				textBoxNoofPLs.Text = "0";
				textBoxAmount.Text = 0.ToString(Format.TotalAmountFormat);
				textBoxAmountBase.Text = 0.ToString(Format.TotalAmountFormat);
				dateTimePickerDate.Value = DateTime.Now;
				datePickerDueDate.Value = dateTimePickerDate.Value.AddDays(int.Parse(numericUpDownTenorDay.Value.ToString()));
				comboBoxCostCenter.Clear();
				textBoxTotalPurchaseClaim.Text = "0.0";
				textBoxTotalQualityClaim.Text = "0.0";
				textBoxTotalBalance.Text = 0.ToString(Format.TotalAmountFormat);
				textBoxTotalDue.Text = 0.ToString(Format.TotalAmountFormat);
				textBoxTerm.Clear();
				linklabelQC.Text = "";
				linklabelPC.Text = "";
				textBoxVoucherNumber.Text = GetNextVoucherNumber();
				textBoxPOVoucherID.Clear();
				comboBoxSysDoc.SetDefaultID(Security.DefaultTransactionLocationID);
				SetApprovalStatus();
				IsVoid = false;
				formManager.ResetDirty();
			}
			catch (Exception e)
			{
				ErrorHelper.ProcessError(e);
			}
		}

		private void JournalLeaveGroupDetailsForm_Validating(object sender, CancelEventArgs e)
		{
		}

		private void JournalLeaveGroupDetailsForm_Validated(object sender, EventArgs e)
		{
		}

		private void buttonDelete_Click(object sender, EventArgs e)
		{
			if (Delete())
			{
				ClearForm();
				IsNewRecord = true;
			}
		}

		private bool Delete()
		{
			try
			{
				if (!allowEdit)
				{
					ErrorHelper.InformationMessage(Application.ProductName, "You cannot delete this transfer transaction because it is already accepted or rejected.", "Document is in use.");
					return false;
				}
				if (ErrorHelper.QuestionMessageYesNo(UIMessages.DeleteRecord) == DialogResult.No)
				{
					return false;
				}
				if (!IsNewRecord && !Factory.TRApplicationSystem.AllowModify(comboBoxSysDoc.SelectedID, textBoxVoucherNumber.Text))
				{
					ErrorHelper.WarningMessage("Some items in this transaction has been already invoiced. You are not able to modify.");
					return false;
				}
				return Factory.TRApplicationSystem.DeleteTRApplication(SystemDocID, textBoxVoucherNumber.Text);
			}
			catch (Exception e)
			{
				ErrorHelper.ProcessError(e);
				return false;
			}
		}

		private void xpButton1_Click(object sender, EventArgs e)
		{
			Close();
		}

		private void toolStripButtonNext_Click(object sender, EventArgs e)
		{
			string nextID = DatabaseHelper.GetNextID("TR_Application", "VoucherID", textBoxVoucherNumber.Text, "SysDocID", SystemDocID);
			if (!(nextID == ""))
			{
				LoadData(nextID);
			}
		}

		private void toolStripButtonPrevious_Click(object sender, EventArgs e)
		{
			string previousID = DatabaseHelper.GetPreviousID("TR_Application", "VoucherID", textBoxVoucherNumber.Text, "SysDocID", SystemDocID);
			if (!(previousID == ""))
			{
				LoadData(previousID);
			}
		}

		private void toolStripButtonLast_Click(object sender, EventArgs e)
		{
			string lastID = DatabaseHelper.GetLastID("TR_Application", "VoucherID", "SysDocID", SystemDocID);
			if (!(lastID == ""))
			{
				LoadData(lastID);
			}
		}

		private void toolStripButtonFirst_Click(object sender, EventArgs e)
		{
			string firstID = DatabaseHelper.GetFirstID("TR_Application", "VoucherID", "SysDocID", SystemDocID);
			if (!(firstID == ""))
			{
				LoadData(firstID);
			}
		}

		private void toolStripButtonFind_Click(object sender, EventArgs e)
		{
			try
			{
				if (toolStripTextBoxFind.Text.Trim() == "")
				{
					toolStripTextBoxFind.Focus();
				}
				else
				{
					string text = Factory.DatabaseSystem.FindDocumentByNumber("TR_Application", "VoucherID", SystemDocID, toolStripTextBoxFind.Text);
					if (text != "")
					{
						LoadData(text);
					}
					else
					{
						ErrorHelper.InformationMessage(UIMessages.DocumentNotFound);
						toolStripTextBoxFind.SelectAll();
						toolStripTextBoxFind.Focus();
					}
				}
			}
			catch (Exception e2)
			{
				ErrorHelper.ProcessError(e2);
			}
		}

		public void OnActivated()
		{
		}

		private void Form_FormClosing(object sender, FormClosingEventArgs e)
		{
			if (!CanClose())
			{
				e.Cancel = true;
			}
		}

		private bool CanClose()
		{
			if (IsDirty)
			{
				BringToFront();
				if (IsNewRecord)
				{
					switch (ErrorHelper.QuestionMessageYesNoCancel(UIMessages.DoYouWantToSave))
					{
					case DialogResult.Yes:
						if (!SaveData())
						{
							return false;
						}
						break;
					default:
						return false;
					case DialogResult.No:
						break;
					}
				}
				else if (!SaveData())
				{
					return false;
				}
			}
			return true;
		}

		private void Form_Load(object sender, EventArgs e)
		{
			try
			{
				comboBoxSysDoc.FilterByType(SysDocTypes.TRApplication);
				SetSecurity();
				if (!base.IsDisposed)
				{
					IsNewRecord = true;
					ClearForm();
				}
			}
			catch (Exception e2)
			{
				ErrorHelper.ProcessError(e2);
			}
		}

		private void SetSecurity()
		{
			screenRight = Security.GetScreenAccessRight(base.Name);
			if (!screenRight.View)
			{
				ErrorHelper.ErrorMessage(UIMessages.NoPermissionView);
				Close();
				return;
			}
			if (!Security.IsAllowedSecurityRole(GeneralSecurityRoles.ChangeDocNumber))
			{
				textBoxVoucherNumber.ReadOnly = true;
			}
			if (!Security.IsAllowedSecurityRole(GeneralSecurityRoles.EditTransaction))
			{
				AllowEditTransaction = false;
			}
			else
			{
				AllowEditTransaction = true;
			}
			if (!Security.IsAllowedSecurityRole(GeneralSecurityRoles.EditTransDiffLocation))
			{
				AllowEditTransDiffLocation = false;
			}
			else
			{
				AllowEditTransDiffLocation = true;
			}
		}

		private string GetNextVoucherNumber()
		{
			try
			{
				return Factory.SystemDocumentSystem.GetNextDocumentNumber(SystemDocID);
			}
			catch (Exception e)
			{
				ErrorHelper.ProcessError(e);
				return "";
			}
		}

		private void buttonVoid_Click(object sender, EventArgs e)
		{
			if (Void(!IsVoid))
			{
				IsVoid = !IsVoid;
			}
		}

		private bool Void(bool isVoid)
		{
			try
			{
				DialogResult dialogResult = (!isVoid) ? ErrorHelper.QuestionMessageYesNo(UIMessages.WantToUnvoid) : ErrorHelper.QuestionMessageYesNo(UIMessages.WantToVoid);
				if (dialogResult == DialogResult.No)
				{
					return false;
				}
				return Factory.TRApplicationSystem.VoidTRApplication(SystemDocID, textBoxVoucherNumber.Text, isVoid);
			}
			catch (Exception e)
			{
				ErrorHelper.ProcessError(e);
				return false;
			}
		}

		private void duplicateToolStripMenuItem_Click(object sender, EventArgs e)
		{
			if (ErrorHelper.QuestionMessageYesNo("Are you sure to duplicate this document?") == DialogResult.Yes)
			{
				string text = textBoxVoucherNumber.Text;
				if (!IsDirty)
				{
					IsNewRecord = true;
					textBoxVoucherNumber.Text = GetNextVoucherNumber();
				}
				else if (CanClose())
				{
					LoadData(text);
					IsNewRecord = true;
					textBoxVoucherNumber.Text = GetNextVoucherNumber();
				}
			}
		}

		private void toolStripDropDownButton1_DropDownOpening(object sender, EventArgs e)
		{
			duplicateToolStripMenuItem.Enabled = !IsNewRecord;
		}

		private void toolStripButtonPrint_Click(object sender, EventArgs e)
		{
			Print(isPrint: true, showPrintDialog: true, saveChanges: true);
		}

		private void Print()
		{
			Print(isPrint: true, showPrintDialog: false, saveChanges: true);
		}

		private void Print(bool isPrint, bool showPrintDialog, bool saveChanges)
		{
			try
			{
				if (!(IsDirty && saveChanges) || (ErrorHelper.QuestionMessage(MessageBoxButtons.YesNo, "You must save the document before printing.", "Do you want to save?") == DialogResult.Yes && SaveData(clearAfter: false)))
				{
					string selectedID = comboBoxSysDoc.SelectedID;
					string text = textBoxVoucherNumber.Text;
					DataSet tRApplicationToPrint = Factory.TRApplicationSystem.GetTRApplicationToPrint(selectedID, text);
					if (tRApplicationToPrint == null || tRApplicationToPrint.Tables.Count == 0)
					{
						ErrorHelper.ErrorMessage("Cannot print the document.", "Document not found.");
					}
					else
					{
						foreach (DataRow row in tRApplicationToPrint.Tables[0].Rows)
						{
							row["AvailableBal"] = decimal.Parse(textBoxRegBalance.Text, NumberStyles.Any);
							row["PayeeBalance"] = TotBalance;
							row["PayeeTotalDue"] = TotDue;
							row["PurchaseClaim"] = textBoxTotalPurchaseClaim.Text;
							row["QualityClaim"] = textBoxTotalQualityClaim.Text;
							row["PCCount"] = totPC;
							row["QCCount"] = totQC;
						}
						PrintHelper.PrintDocument(tRApplicationToPrint, selectedID, "TR Application", SysDocTypes.TRApplication, isPrint, showPrintDialog);
					}
				}
			}
			catch (Exception e)
			{
				ErrorHelper.ProcessError(e);
			}
		}

		private void toolStripButtonPreview_Click(object sender, EventArgs e)
		{
			Print(isPrint: false, showPrintDialog: false, saveChanges: true);
		}

		public void EditDocument(string sysDocID, string voucherID)
		{
			if (!comboBoxSysDoc.Enabled && sysDocID != comboBoxSysDoc.SelectedID)
			{
				ErrorHelper.ErrorMessage("Cannot edit this document because you do not have access to this document.");
				return;
			}
			comboBoxSysDoc.SelectedID = sysDocID;
			LoadData(voucherID);
		}

		private void transferToPaymentRequestToolStripMenuItem_Click(object sender, EventArgs e)
		{
		}

		private void toolStripButtonOpenList_Click(object sender, EventArgs e)
		{
			FormActivator.BringFormToFront(FormActivator.TRApplicationListFormObj);
		}

		private void saveDraftToolStripMenuItem_Click(object sender, EventArgs e)
		{
			try
			{
				if (GetData())
				{
					EnterNameDialog enterNameDialog = new EnterNameDialog();
					if (enterNameDialog.ShowDialog() == DialogResult.OK)
					{
						Global.CompanySettings.SaveTransactionDraft(currentData, enterNameDialog.EnteredName, SysDocTypes.PaymentRequest);
					}
				}
			}
			catch
			{
				throw;
			}
		}

		private bool LoadDraft()
		{
			try
			{
				DataSet settingsList = Factory.SettingSystem.GetSettingsList("", 100.ToString());
				SelectDocumentDialog selectDocumentDialog = new SelectDocumentDialog();
				selectDocumentDialog.DataSource = settingsList;
				selectDocumentDialog.Text = "Select Draft";
				selectDocumentDialog.IsMultiSelect = false;
				if (selectDocumentDialog.ShowDialog(this) == DialogResult.OK)
				{
					string key = selectDocumentDialog.SelectedRow.Cells["Name"].Value.ToString();
					DataSet dataSet = Global.CompanySettings.LoadTransactionDraft(key, SysDocTypes.PaymentRequest);
					currentData = (dataSet as TRApplicationData);
					FillData();
				}
				return true;
			}
			catch (Exception e)
			{
				ErrorHelper.ProcessError(e);
				return false;
			}
		}

		private void loadDraftToolStripMenuItem_Click(object sender, EventArgs e)
		{
			LoadDraft();
		}

		private void toolStripButtonAttach_Click(object sender, EventArgs e)
		{
			try
			{
				if (!isNewRecord)
				{
					DocManagementForm docManagementForm = new DocManagementForm();
					docManagementForm.EntityID = comboBoxSysDoc.SelectedID + textBoxVoucherNumber.Text.Trim();
					docManagementForm.EntitySysDocID = comboBoxSysDoc.SelectedID;
					docManagementForm.EntityName = comboBoxSysDoc.SelectedID;
					docManagementForm.EntityType = EntityTypesEnum.Transactions;
					docManagementForm.ShowDialog(this);
				}
			}
			catch (Exception e2)
			{
				ErrorHelper.ProcessError(e2);
			}
		}

		private void toolStripButtonDistribution_Click(object sender, EventArgs e)
		{
			JournalDistibutionDialog journalDistibutionDialog = new JournalDistibutionDialog();
			journalDistibutionDialog.VoucherID = textBoxVoucherNumber.Text;
			journalDistibutionDialog.SysDocID = comboBoxSysDoc.SelectedID;
			journalDistibutionDialog.ShowDialog(this);
		}

		private void toolStripButtonInformation_Click(object sender, EventArgs e)
		{
			DocumentInformationDialog documentInformationDialog = new DocumentInformationDialog();
			documentInformationDialog.VoucherID = textBoxVoucherNumber.Text;
			documentInformationDialog.SysDocID = comboBoxSysDoc.SelectedID;
			documentInformationDialog.ShowDialog(this);
		}

		private void buttonSelectPO_Click(object sender, EventArgs e)
		{
			try
			{
				if (comboBoxVendor.SelectedID == "")
				{
					ErrorHelper.InformationMessage("Please select a vendor.");
				}
				else
				{
					SelectDocumentDialog selectDocumentDialog = new SelectDocumentDialog();
					selectDocumentDialog.Text = "Select Purchase Order";
					selectDocumentDialog.DataSource = Factory.PurchaseOrderSystem.GetPOListForPayment(comboBoxVendor.SelectedID);
					if (selectDocumentDialog.ShowDialog(this) == DialogResult.OK)
					{
						textBoxPOSysDocID.Text = selectDocumentDialog.SelectedRow.Cells["SysDocID"].Value.ToString();
						textBoxPOVoucherID.Text = selectDocumentDialog.SelectedRow.Cells["VoucherID"].Value.ToString();
						FillPOData();
					}
				}
			}
			catch (Exception e2)
			{
				ErrorHelper.ProcessError(e2);
			}
		}

		private void FillPOData()
		{
			try
			{
				if (!(textBoxPOVoucherID.Text == ""))
				{
					DataSet pOPaymentSummary = Factory.PurchaseOrderSystem.GetPOPaymentSummary(textBoxPOSysDocID.Text, textBoxPOVoucherID.Text, SystemDocID, textBoxVoucherNumber.Text);
					if (pOPaymentSummary != null && pOPaymentSummary.Tables[0].Rows.Count > 0)
					{
						DataRow dataRow = pOPaymentSummary.Tables[0].Rows[0];
						decimal d = decimal.Parse(dataRow["Total"].ToString());
						decimal d2 = decimal.Parse(dataRow["PaidAmount"].ToString());
						textBoxPOAmount.Text = d.ToString(Format.TotalAmountFormat);
						textBoxPOPaid.Text = d2.ToString(Format.TotalAmountFormat);
						textBoxPOBalance.Text = (d - d2).ToString(Format.TotalAmountFormat);
						comboBoxPOTerm.SelectedID = dataRow["TermID"].ToString();
						if (dataRow["ETA"].ToString() != "" && dataRow["ETA"].ToString() != string.Empty)
						{
							DateTime dateTime = DateTime.Parse(dataRow["ETA"].ToString());
							dateTimePickerETA.Text = dateTime.ToShortDateString();
						}
					}
				}
			}
			catch (Exception e)
			{
				ErrorHelper.ProcessError(e);
			}
		}

		private void ultraFormattedLinkLabel1_LinkClicked(object sender, Infragistics.Win.FormattedLinkLabel.LinkClickedEventArgs e)
		{
			new FormHelper();
		}

		private void ultraFormattedLinkLabel4_LinkClicked(object sender, Infragistics.Win.FormattedLinkLabel.LinkClickedEventArgs e)
		{
			new FormHelper().EditVendor(comboBoxVendor.SelectedID);
		}

		private void comboBoxType_SelectedValueChanged(object sender, EventArgs e)
		{
		}

		private void ultraFormattedLinkLabel5_LinkClicked(object sender, Infragistics.Win.FormattedLinkLabel.LinkClickedEventArgs e)
		{
			new FormHelper().EditSysDoc(comboBoxSysDoc.SelectedID, SysDocTypes.TRApplication);
		}

		private void ultraFormattedLinkLabel2_LinkClicked(object sender, Infragistics.Win.FormattedLinkLabel.LinkClickedEventArgs e)
		{
			if (isNewRecord)
			{
				textBoxVoucherNumber.Text = GetNextVoucherNumber();
			}
		}

		private void ultraFormattedLinkLabel3_LinkClicked(object sender, Infragistics.Win.FormattedLinkLabel.LinkClickedEventArgs e)
		{
			new FormHelper().EditVendor(comboBoxVendor.SelectedID);
		}

		private void buttonSelectRequest_Click(object sender, EventArgs e)
		{
			try
			{
				DataSet openPaymentRequests = Factory.PaymentRequestSystem.GetOpenPaymentRequests(3);
				SelectDocumentDialog selectDocumentDialog = new SelectDocumentDialog();
				selectDocumentDialog.DataSource = openPaymentRequests;
				selectDocumentDialog.IsMultiSelect = false;
				selectDocumentDialog.Text = "Select Payment Request";
				if (selectDocumentDialog.ShowDialog(this) == DialogResult.OK)
				{
					UltraGridRow activeRow = selectDocumentDialog.Grid.ActiveRow;
					string sysDocID = activeRow.Cells["DocID"].Value.ToString();
					string text = activeRow.Cells["Number"].Value.ToString();
					PaymentRequestData paymentRequestByID = Factory.PaymentRequestSystem.GetPaymentRequestByID(sysDocID, text);
					if (paymentRequestByID != null && paymentRequestByID.Tables[0].Rows.Count > 0)
					{
						DataRow dataRow = paymentRequestByID.Tables[0].Rows[0];
						textBoxRequest.Text = text;
						requestSysDocID = sysDocID;
						comboBoxVendor.SelectedID = dataRow["PayeeID"].ToString();
						comboBoxFacility.SelectedID = dataRow["PayFromID"].ToString();
						if (!dataRow["AmountFC"].IsDBNullOrEmpty())
						{
							textBoxAmount.Text = dataRow["AmountFC"].ToString();
						}
						else
						{
							textBoxAmount.Text = dataRow["Amount"].ToString();
						}
						currencySelector.SelectedID = dataRow["CurrencyID"].ToString();
						comboBoxVendor.Enabled = false;
						comboBoxFacility.Enabled = false;
						textBoxPOSysDocID.Text = dataRow["POSysDocID"].ToString();
						textBoxPOVoucherID.Text = dataRow["POVoucherID"].ToString();
						comboBoxReason.SelectedIndex = checked(int.Parse(dataRow["Reason"].ToString()) - 1);
						textBoxNote.Text = dataRow["Note"].ToString();
						textBoxInvoiceNo.Text = dataRow["InvoiceNos"].ToString();
						textBoxAuthorizedby.Text = dataRow["Authorizedby"].ToString();
						textBoxNoofInvoices.Text = dataRow["NoofInvoices"].ToString();
						textBoxNoofPLs.Text = dataRow["NoofPL"].ToString();
						textBoxNoofBOLs.Text = dataRow["NoofBOL"].ToString();
						textBoxNoofGoods.Text = dataRow["NoofGoods"].ToString();
					}
					FillPOData();
				}
			}
			catch (Exception e2)
			{
				ErrorHelper.ProcessError(e2);
			}
		}

		private void comboBoxFacility_SelectedIndexChanged(object sender, EventArgs e)
		{
			if (comboBoxFacility.SelectedID == "")
			{
				textBoxRegBalance.Clear();
				return;
			}
			decimal availableLimit = comboBoxFacility.AvailableLimit;
			textBoxRegBalance.Text = availableLimit.ToString(Format.TotalAmountFormat, CultureInfo.CurrentCulture);
			numericUpDownTenorDay.Value = comboBoxFacility.TenorDays;
		}

		private void numericUpDownTenorDay_ValueChanged(object sender, EventArgs e)
		{
			datePickerDueDate.Value = dateTimePickerDate.Value.AddDays(int.Parse(numericUpDownTenorDay.Value.ToString()));
		}

		private void toolStripButtonMultiPreview_Click(object sender, EventArgs e)
		{
			AttachementDetailsForm attachementDetailsForm = new AttachementDetailsForm();
			attachementDetailsForm.SysDocID = comboBoxSysDoc.SelectedID;
			attachementDetailsForm.VoucherID = textBoxVoucherNumber.Text;
			attachementDetailsForm.SysDocType = SysDocTypes.TRApplication;
			attachementDetailsForm.FormType = "Transaction";
			attachementDetailsForm.Show();
		}

		private void linklabelQC_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
		{
			DataSet openQualityClaims = Factory.QualityClaimSystem.GetOpenQualityClaims(comboBoxVendor.SelectedID);
			SelectDocumentDialog selectDocumentDialog = new SelectDocumentDialog();
			selectDocumentDialog.DataSource = openQualityClaims;
			selectDocumentDialog.Text = "Select Quality Claim";
			if (selectDocumentDialog.ShowDialog(this) == DialogResult.OK)
			{
				string sysDocID = selectDocumentDialog.SelectedRow.Cells["Doc ID"].Value.ToString();
				string text = selectDocumentDialog.SelectedRow.Cells["Number"].Value.ToString();
				FormActivator.BringFormToFront(FormActivator.QualityClaimFormObj);
				if (text != "")
				{
					FormActivator.QualityClaimFormObj.EditDocument(sysDocID, text);
				}
			}
		}

		private void linklabelPC_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
		{
			DataSet openPurchaseClaims = Factory.PurchaseClaimSystem.GetOpenPurchaseClaims(comboBoxVendor.SelectedID);
			SelectDocumentDialog selectDocumentDialog = new SelectDocumentDialog();
			selectDocumentDialog.DataSource = openPurchaseClaims;
			selectDocumentDialog.Text = "Select Purchase Claim";
			if (selectDocumentDialog.ShowDialog(this) == DialogResult.OK)
			{
				string sysDocID = selectDocumentDialog.SelectedRow.Cells["Doc ID"].Value.ToString();
				string text = selectDocumentDialog.SelectedRow.Cells["Number"].Value.ToString();
				FormActivator.BringFormToFront(FormActivator.PurchaseClaimFormObj);
				if (text != "")
				{
					FormActivator.PurchaseClaimFormObj.EditDocument(sysDocID, text);
				}
			}
		}

		private void toolStripTextBoxFind_KeyPress(object sender, KeyPressEventArgs e)
		{
			if (e.KeyChar == Convert.ToChar(Keys.Return))
			{
				toolStripButtonFind_Click(sender, e);
			}
		}

		private void xpButton2_Click(object sender, EventArgs e)
		{
		}

		private void buttonSelectInvoice_Click(object sender, EventArgs e)
		{
			string text = "";
			text = comboBoxVendor.SelectedID;
			SelectInvoicesToPay(text, comboBoxVendor.SelectedName, currencySelector.SelectedID);
		}

		private void toolStripButtonPrintTemplate_Click(object sender, EventArgs e)
		{
		}

		private void toolStripButtonInformation_Click_1(object sender, EventArgs e)
		{
			if (!isNewRecord)
			{
				FormHelper.ShowDocumentInfo(textBoxVoucherNumber.Text, comboBoxSysDoc.SelectedID, this);
			}
		}

		private void SelectInvoicesToPay(string vendorID, string vendorName, string currencyID)
		{
			try
			{
				if (vendorID != "")
				{
					PaymentAdviceDetailsForm paymentAdviceDetailsForm = new PaymentAdviceDetailsForm();
					paymentAdviceDetailsForm.IsARPayment = false;
					paymentAdviceDetailsForm.SetData(vendorID, vendorName, currencyID, currencySelector.Rate);
					if (paymentAdviceDetailsForm.ShowDialog() == DialogResult.OK)
					{
						DataSet dataSet = new DataSet();
						DataTable dataTable = dataSet.Tables.Add("Invoice");
						dataTable.Columns.AddRange(new DataColumn[2]
						{
							new DataColumn("SysDocID"),
							new DataColumn("VoucherID")
						});
						foreach (DataRow row in paymentAdviceDetailsForm.PaymentData.Tables["AP_Payment_Advice"].Rows)
						{
							dataTable.Rows.Add(row["InvoiceSysDocID"].ToString(), row["InvoiceVoucherID"].ToString());
						}
						string text = Factory.PurchasePrepaymentInvoiceSystem.HasPendingPrepayments(dataSet);
						if (!(text != "") || ErrorHelper.WarningMessageYesNo("Invoice number '" + text + "' has unallocated prepayments.", "Are you sure you want to continue?") != DialogResult.No)
						{
							textBoxAmount.Tag = paymentAdviceDetailsForm.PaymentData;
							decimal d = default(decimal);
							foreach (DataRow row2 in paymentAdviceDetailsForm.PaymentData.Tables["AP_Payment_Advice"].Rows)
							{
								d += decimal.Parse(row2["PaymentAmount"].ToString());
							}
							textBoxAmount.Text = d.ToString(Format.TotalAmountFormat);
							if (d > 0m)
							{
								textBoxAmount.ReadOnly = true;
								currencySelector.Enabled = false;
							}
						}
					}
				}
				else
				{
					ErrorHelper.InformationMessage("Please select a vendor.");
				}
			}
			catch (Exception e)
			{
				ErrorHelper.ProcessError(e);
			}
		}

		protected override void Dispose(bool disposing)
		{
			if (disposing && components != null)
			{
				components.Dispose();
			}
			base.Dispose(disposing);
		}

		private void InitializeComponent()
		{
			components = new System.ComponentModel.Container();
			Infragistics.Win.Appearance appearance = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance2 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance3 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance4 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance5 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance6 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance7 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance8 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance9 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance10 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance11 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance12 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance13 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance14 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance15 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance16 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance17 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance18 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance19 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance20 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance21 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance22 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance23 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance24 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance25 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance26 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance27 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance28 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance29 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance30 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance31 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance32 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance33 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance34 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance35 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance36 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance37 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance38 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance39 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance40 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance41 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance42 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance43 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance44 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance45 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance46 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance47 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance48 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance49 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance50 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance51 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance52 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance53 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance54 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance55 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance56 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance57 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance58 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance59 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance60 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance61 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance62 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance63 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance64 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance65 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance66 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance67 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance68 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance69 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance70 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance71 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance72 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance73 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance74 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance75 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance76 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance77 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance78 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance79 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance80 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance81 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance82 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance83 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance84 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance85 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance86 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance87 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance88 = new Infragistics.Win.Appearance();
			System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Micromind.ClientUI.WindowsForms.DataEntries.Accounts.TRApplicationForm));
			Infragistics.Win.Appearance appearance89 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance90 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance91 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance92 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance93 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance94 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance95 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance96 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance97 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance98 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance99 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance100 = new Infragistics.Win.Appearance();
			ultraFormattedLinkLabel8 = new Infragistics.Win.FormattedLinkLabel.UltraFormattedLinkLabel();
			ultraFormattedLinkLabel4 = new Infragistics.Win.FormattedLinkLabel.UltraFormattedLinkLabel();
			numericUpDownTenorDay = new System.Windows.Forms.NumericUpDown();
			textBoxRegBalance = new System.Windows.Forms.TextBox();
			label19 = new System.Windows.Forms.Label();
			textBoxRef1 = new System.Windows.Forms.TextBox();
			labelAmountBase = new System.Windows.Forms.Label();
			label21 = new System.Windows.Forms.Label();
			textBoxAmountBase = new System.Windows.Forms.TextBox();
			label22 = new System.Windows.Forms.Label();
			textBoxFacilityName = new System.Windows.Forms.TextBox();
			textBoxInvoiceNo = new System.Windows.Forms.TextBox();
			labelInvnos = new System.Windows.Forms.Label();
			textBoxNote = new System.Windows.Forms.TextBox();
			label3 = new System.Windows.Forms.Label();
			panelTR = new System.Windows.Forms.Panel();
			labelVoided = new System.Windows.Forms.Label();
			textBoxNoofGoods = new System.Windows.Forms.TextBox();
			textBoxNoofPLs = new Micromind.UISupport.NumberTextBox();
			textBoxNoofBOLs = new Micromind.UISupport.NumberTextBox();
			label18 = new System.Windows.Forms.Label();
			label17 = new System.Windows.Forms.Label();
			label16 = new System.Windows.Forms.Label();
			textBoxNoofInvoices = new Micromind.UISupport.NumberTextBox();
			label15 = new System.Windows.Forms.Label();
			label14 = new System.Windows.Forms.Label();
			textBoxAuthorizedby = new System.Windows.Forms.TextBox();
			comboBoxReason = new System.Windows.Forms.ComboBox();
			label2 = new System.Windows.Forms.Label();
			panelButtons = new System.Windows.Forms.Panel();
			buttonVoid = new Micromind.UISupport.XPButton();
			buttonDelete = new Micromind.UISupport.XPButton();
			buttonNew = new Micromind.UISupport.XPButton();
			linePanelDown = new Micromind.UISupport.Line();
			xpButton1 = new Micromind.UISupport.XPButton();
			buttonSave = new Micromind.UISupport.XPButton();
			contextMenuStrip1 = new System.Windows.Forms.ContextMenuStrip(components);
			availableQuantityToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
			salesStatisticsToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
			itemPicToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
			itemDetailsToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
			toolStripSeparator3 = new System.Windows.Forms.ToolStripSeparator();
			removeRowToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
			panelDetails = new System.Windows.Forms.Panel();
			textBoxTotalQualityClaim = new System.Windows.Forms.Label();
			textBoxTotalPurchaseClaim = new System.Windows.Forms.Label();
			linklabelPC = new Micromind.UISupport.BALinkLabel();
			linklabelQC = new Micromind.UISupport.BALinkLabel();
			mmLabel6 = new Micromind.UISupport.MMLabel();
			mmLabel3 = new Micromind.UISupport.MMLabel();
			label10 = new System.Windows.Forms.Label();
			mmLabel4 = new Micromind.UISupport.MMLabel();
			textBoxTotalDue = new Micromind.UISupport.AmountTextBox();
			labelVendorBalance = new Micromind.UISupport.MMLabel();
			textBoxTotalBalance = new Micromind.UISupport.AmountTextBox();
			textBoxTerm = new System.Windows.Forms.TextBox();
			buttonSelectRequest = new Micromind.UISupport.XPButton();
			ultraFormattedLinkLabel1 = new Infragistics.Win.FormattedLinkLabel.UltraFormattedLinkLabel();
			textBoxRequest = new System.Windows.Forms.TextBox();
			ultraFormattedLinkLabel5 = new Infragistics.Win.FormattedLinkLabel.UltraFormattedLinkLabel();
			comboBoxVendor = new Micromind.DataControls.vendorsFlatComboBox();
			mmLabel1 = new Micromind.UISupport.MMLabel();
			label1 = new System.Windows.Forms.Label();
			currencySelector = new Micromind.DataControls.CurrencySelector();
			textBoxDescription = new System.Windows.Forms.TextBox();
			textBoxTRNote = new System.Windows.Forms.TextBox();
			label4 = new System.Windows.Forms.Label();
			labelCurrency = new Infragistics.Win.FormattedLinkLabel.UltraFormattedLinkLabel();
			ultraFormattedLinkLabel2 = new Infragistics.Win.FormattedLinkLabel.UltraFormattedLinkLabel();
			ultraFormattedLinkLabel3 = new Infragistics.Win.FormattedLinkLabel.UltraFormattedLinkLabel();
			dateTimePickerDate = new Micromind.UISupport.flatDatePicker();
			textBoxVoucherNumber = new System.Windows.Forms.TextBox();
			comboBoxCostCenter = new Micromind.DataControls.CostCenterComboBox();
			textBoxPayeeName = new System.Windows.Forms.TextBox();
			ultraFormattedLinkLabel6 = new Infragistics.Win.FormattedLinkLabel.UltraFormattedLinkLabel();
			comboBoxSysDoc = new Micromind.DataControls.SysDocComboBox();
			comboBoxVendorTerm = new Micromind.DataControls.PaymentTermComboBox();
			panel1 = new System.Windows.Forms.Panel();
			panelPO = new System.Windows.Forms.Panel();
			dateTimePickerETA = new System.Windows.Forms.TextBox();
			label13 = new System.Windows.Forms.Label();
			textBoxPOSysDocID = new System.Windows.Forms.TextBox();
			buttonSelectPO = new Micromind.UISupport.XPButton();
			textBoxPOVoucherID = new System.Windows.Forms.TextBox();
			label9 = new System.Windows.Forms.Label();
			textBoxPOTerm = new System.Windows.Forms.TextBox();
			label8 = new System.Windows.Forms.Label();
			textBoxPOBalance = new Micromind.UISupport.AmountTextBox();
			label7 = new System.Windows.Forms.Label();
			textBoxPOPaid = new Micromind.UISupport.AmountTextBox();
			label6 = new System.Windows.Forms.Label();
			textBoxPOAmount = new Micromind.UISupport.AmountTextBox();
			label5 = new System.Windows.Forms.Label();
			paymentTermComboBox1 = new Micromind.DataControls.PaymentTermComboBox();
			comboBoxPOTerm = new Micromind.DataControls.PaymentTermComboBox();
			toolStripButtonFirst = new System.Windows.Forms.ToolStripButton();
			toolStripButtonPrevious = new System.Windows.Forms.ToolStripButton();
			toolStripButtonNext = new System.Windows.Forms.ToolStripButton();
			toolStripButtonLast = new System.Windows.Forms.ToolStripButton();
			toolStripSeparator1 = new System.Windows.Forms.ToolStripSeparator();
			toolStripButtonOpenList = new System.Windows.Forms.ToolStripButton();
			toolStripSeparator5 = new System.Windows.Forms.ToolStripSeparator();
			toolStripTextBoxFind = new System.Windows.Forms.ToolStripTextBox();
			toolStripButtonFind = new System.Windows.Forms.ToolStripButton();
			toolStripSeparator2 = new System.Windows.Forms.ToolStripSeparator();
			toolStripButtonPreview = new System.Windows.Forms.ToolStripButton();
			toolStripButtonPrint = new System.Windows.Forms.ToolStripButton();
			toolStripSeparator7 = new System.Windows.Forms.ToolStripSeparator();
			toolStripButtonAttach = new System.Windows.Forms.ToolStripButton();
			toolStripSeparator4 = new System.Windows.Forms.ToolStripSeparator();
			toolStripDropDownButton1 = new System.Windows.Forms.ToolStripDropDownButton();
			duplicateToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
			toolStripSeparator6 = new System.Windows.Forms.ToolStripSeparator();
			saveDraftToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
			loadDraftToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
			toolStripButtonApproval = new System.Windows.Forms.ToolStripButton();
			toolStripLabelApproval = new System.Windows.Forms.ToolStripLabel();
			toolStripSeparatorApproval = new System.Windows.Forms.ToolStripSeparator();
			toolStripButtonPrintTemplate = new System.Windows.Forms.ToolStripButton();
			toolStripButtonInformation = new System.Windows.Forms.ToolStripButton();
			toolStrip1 = new System.Windows.Forms.ToolStrip();
			toolStripButtonMultiPreview = new System.Windows.Forms.ToolStripButton();
			buttonSelectInvoice = new Micromind.UISupport.XPButton();
			formManager = new Micromind.DataControls.FormManager();
			datePickerDueDate = new Micromind.UISupport.flatDatePicker();
			textBoxAmount = new Micromind.UISupport.AmountTextBox();
			mmLabel7 = new Micromind.UISupport.MMLabel();
			comboBoxFacility = new Micromind.DataControls.BankFacilityComboBox();
			((System.ComponentModel.ISupportInitialize)numericUpDownTenorDay).BeginInit();
			panelTR.SuspendLayout();
			panelButtons.SuspendLayout();
			contextMenuStrip1.SuspendLayout();
			panelDetails.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)comboBoxVendor).BeginInit();
			((System.ComponentModel.ISupportInitialize)comboBoxCostCenter).BeginInit();
			((System.ComponentModel.ISupportInitialize)comboBoxSysDoc).BeginInit();
			((System.ComponentModel.ISupportInitialize)comboBoxVendorTerm).BeginInit();
			panel1.SuspendLayout();
			panelPO.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)paymentTermComboBox1).BeginInit();
			((System.ComponentModel.ISupportInitialize)comboBoxPOTerm).BeginInit();
			toolStrip1.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)comboBoxFacility).BeginInit();
			SuspendLayout();
			appearance.FontData.BoldAsString = "True";
			appearance.FontData.Name = "Tahoma";
			ultraFormattedLinkLabel8.Appearance = appearance;
			ultraFormattedLinkLabel8.AutoSize = true;
			ultraFormattedLinkLabel8.Location = new System.Drawing.Point(15, 254);
			ultraFormattedLinkLabel8.Name = "ultraFormattedLinkLabel8";
			ultraFormattedLinkLabel8.Size = new System.Drawing.Size(52, 15);
			ultraFormattedLinkLabel8.TabIndex = 163;
			ultraFormattedLinkLabel8.TabStop = true;
			ultraFormattedLinkLabel8.TreatValueAs = Infragistics.Win.FormattedLinkLabel.TreatValueAs.URL;
			ultraFormattedLinkLabel8.UnderlineLinks = Infragistics.Win.FormattedLinkLabel.UnderlineLink.WhenHovered;
			ultraFormattedLinkLabel8.Value = "Amount:";
			appearance2.ForeColor = System.Drawing.Color.Blue;
			ultraFormattedLinkLabel8.VisitedLinkAppearance = appearance2;
			appearance3.BackColor = System.Drawing.Color.Transparent;
			appearance3.FontData.BoldAsString = "True";
			appearance3.FontData.Name = "Tahoma";
			ultraFormattedLinkLabel4.Appearance = appearance3;
			ultraFormattedLinkLabel4.AutoSize = true;
			ultraFormattedLinkLabel4.Location = new System.Drawing.Point(14, 209);
			ultraFormattedLinkLabel4.Name = "ultraFormattedLinkLabel4";
			ultraFormattedLinkLabel4.Size = new System.Drawing.Size(60, 15);
			ultraFormattedLinkLabel4.TabIndex = 121;
			ultraFormattedLinkLabel4.TabStop = true;
			ultraFormattedLinkLabel4.TreatValueAs = Infragistics.Win.FormattedLinkLabel.TreatValueAs.URL;
			ultraFormattedLinkLabel4.UnderlineLinks = Infragistics.Win.FormattedLinkLabel.UnderlineLink.WhenHovered;
			ultraFormattedLinkLabel4.Value = "Pay From:";
			appearance4.ForeColor = System.Drawing.Color.Blue;
			ultraFormattedLinkLabel4.VisitedLinkAppearance = appearance4;
			ultraFormattedLinkLabel4.LinkClicked += new Infragistics.Win.FormattedLinkLabel.LinkClickedEventHandler(ultraFormattedLinkLabel4_LinkClicked);
			numericUpDownTenorDay.Location = new System.Drawing.Point(326, 228);
			numericUpDownTenorDay.Maximum = new decimal(new int[4]
			{
				500,
				0,
				0,
				0
			});
			numericUpDownTenorDay.Name = "numericUpDownTenorDay";
			numericUpDownTenorDay.Size = new System.Drawing.Size(61, 20);
			numericUpDownTenorDay.TabIndex = 6;
			numericUpDownTenorDay.Value = new decimal(new int[4]
			{
				30,
				0,
				0,
				0
			});
			numericUpDownTenorDay.ValueChanged += new System.EventHandler(numericUpDownTenorDay_ValueChanged);
			textBoxRegBalance.BackColor = System.Drawing.Color.WhiteSmoke;
			textBoxRegBalance.Location = new System.Drawing.Point(481, 206);
			textBoxRegBalance.Name = "textBoxRegBalance";
			textBoxRegBalance.ReadOnly = true;
			textBoxRegBalance.Size = new System.Drawing.Size(133, 20);
			textBoxRegBalance.TabIndex = 3;
			textBoxRegBalance.TabStop = false;
			textBoxRegBalance.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
			label19.AutoSize = true;
			label19.BackColor = System.Drawing.Color.Transparent;
			label19.Location = new System.Drawing.Point(259, 231);
			label19.Name = "label19";
			label19.Size = new System.Drawing.Size(65, 13);
			label19.TabIndex = 135;
			label19.Text = "Tenor Days:";
			textBoxRef1.Location = new System.Drawing.Point(100, 229);
			textBoxRef1.MaxLength = 15;
			textBoxRef1.Name = "textBoxRef1";
			textBoxRef1.Size = new System.Drawing.Size(111, 20);
			textBoxRef1.TabIndex = 4;
			labelAmountBase.AutoSize = true;
			labelAmountBase.BackColor = System.Drawing.Color.Transparent;
			labelAmountBase.Location = new System.Drawing.Point(261, 257);
			labelAmountBase.Name = "labelAmountBase";
			labelAmountBase.Size = new System.Drawing.Size(71, 13);
			labelAmountBase.TabIndex = 135;
			labelAmountBase.Text = "Amount AED:";
			label21.AutoSize = true;
			label21.BackColor = System.Drawing.Color.Transparent;
			label21.Location = new System.Drawing.Point(12, 231);
			label21.Name = "label21";
			label21.Size = new System.Drawing.Size(45, 13);
			label21.TabIndex = 20;
			label21.Text = "TR Ref:";
			textBoxAmountBase.BackColor = System.Drawing.Color.WhiteSmoke;
			textBoxAmountBase.Location = new System.Drawing.Point(359, 254);
			textBoxAmountBase.Name = "textBoxAmountBase";
			textBoxAmountBase.ReadOnly = true;
			textBoxAmountBase.Size = new System.Drawing.Size(131, 20);
			textBoxAmountBase.TabIndex = 8;
			textBoxAmountBase.TabStop = false;
			textBoxAmountBase.Text = "0.00";
			textBoxAmountBase.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
			label22.AutoSize = true;
			label22.BackColor = System.Drawing.Color.Transparent;
			label22.Location = new System.Drawing.Point(444, 208);
			label22.Name = "label22";
			label22.Size = new System.Drawing.Size(31, 13);
			label22.TabIndex = 129;
			label22.Text = "Limit:";
			textBoxFacilityName.BackColor = System.Drawing.Color.WhiteSmoke;
			textBoxFacilityName.Location = new System.Drawing.Point(214, 206);
			textBoxFacilityName.Name = "textBoxFacilityName";
			textBoxFacilityName.ReadOnly = true;
			textBoxFacilityName.Size = new System.Drawing.Size(226, 20);
			textBoxFacilityName.TabIndex = 2;
			textBoxFacilityName.TabStop = false;
			textBoxInvoiceNo.Location = new System.Drawing.Point(96, 99);
			textBoxInvoiceNo.MaxLength = 15;
			textBoxInvoiceNo.Name = "textBoxInvoiceNo";
			textBoxInvoiceNo.Size = new System.Drawing.Size(511, 20);
			textBoxInvoiceNo.TabIndex = 9;
			labelInvnos.AutoSize = true;
			labelInvnos.Location = new System.Drawing.Point(9, 102);
			labelInvnos.Name = "labelInvnos";
			labelInvnos.Size = new System.Drawing.Size(67, 13);
			labelInvnos.TabIndex = 202;
			labelInvnos.Text = "Invoice Nos:";
			textBoxNote.Location = new System.Drawing.Point(96, 77);
			textBoxNote.MaxLength = 1000;
			textBoxNote.Name = "textBoxNote";
			textBoxNote.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
			textBoxNote.Size = new System.Drawing.Size(511, 20);
			textBoxNote.TabIndex = 8;
			label3.AutoSize = true;
			label3.Location = new System.Drawing.Point(9, 80);
			label3.Name = "label3";
			label3.Size = new System.Drawing.Size(33, 13);
			label3.TabIndex = 20;
			label3.Text = "Note:";
			panelTR.Controls.Add(labelVoided);
			panelTR.Controls.Add(textBoxNoofGoods);
			panelTR.Controls.Add(textBoxNoofPLs);
			panelTR.Controls.Add(textBoxNoofBOLs);
			panelTR.Controls.Add(label18);
			panelTR.Controls.Add(label17);
			panelTR.Controls.Add(label16);
			panelTR.Controls.Add(textBoxNoofInvoices);
			panelTR.Controls.Add(label15);
			panelTR.Controls.Add(label14);
			panelTR.Controls.Add(textBoxAuthorizedby);
			panelTR.Location = new System.Drawing.Point(6, 121);
			panelTR.Name = "panelTR";
			panelTR.Size = new System.Drawing.Size(598, 73);
			panelTR.TabIndex = 22;
			labelVoided.Anchor = (System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left);
			labelVoided.BackColor = System.Drawing.Color.Transparent;
			labelVoided.Font = new System.Drawing.Font("Microsoft Sans Serif", 14f, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0);
			labelVoided.ForeColor = System.Drawing.Color.DarkRed;
			labelVoided.Location = new System.Drawing.Point(481, 44);
			labelVoided.Name = "labelVoided";
			labelVoided.Size = new System.Drawing.Size(91, 21);
			labelVoided.TabIndex = 213;
			labelVoided.Text = "VOIDED";
			labelVoided.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
			labelVoided.Visible = false;
			textBoxNoofGoods.Location = new System.Drawing.Point(90, 24);
			textBoxNoofGoods.MaxLength = 30;
			textBoxNoofGoods.Name = "textBoxNoofGoods";
			textBoxNoofGoods.Size = new System.Drawing.Size(119, 20);
			textBoxNoofGoods.TabIndex = 1;
			textBoxNoofPLs.AllowDecimal = true;
			textBoxNoofPLs.CustomReportFieldName = "";
			textBoxNoofPLs.CustomReportKey = "";
			textBoxNoofPLs.CustomReportValueType = 1;
			textBoxNoofPLs.IsComboTextBox = false;
			textBoxNoofPLs.IsModified = false;
			textBoxNoofPLs.Location = new System.Drawing.Point(90, 47);
			textBoxNoofPLs.MaxLength = 7;
			textBoxNoofPLs.MaxValue = new decimal(new int[4]
			{
				-1,
				-1,
				-1,
				0
			});
			textBoxNoofPLs.MinValue = new decimal(new int[4]
			{
				-1,
				-1,
				-1,
				-2147483648
			});
			textBoxNoofPLs.Name = "textBoxNoofPLs";
			textBoxNoofPLs.NullText = "0";
			textBoxNoofPLs.Size = new System.Drawing.Size(62, 20);
			textBoxNoofPLs.TabIndex = 2;
			textBoxNoofPLs.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
			textBoxNoofBOLs.AllowDecimal = true;
			textBoxNoofBOLs.CustomReportFieldName = "";
			textBoxNoofBOLs.CustomReportKey = "";
			textBoxNoofBOLs.CustomReportValueType = 1;
			textBoxNoofBOLs.IsComboTextBox = false;
			textBoxNoofBOLs.IsModified = false;
			textBoxNoofBOLs.Location = new System.Drawing.Point(317, 4);
			textBoxNoofBOLs.MaxLength = 7;
			textBoxNoofBOLs.MaxValue = new decimal(new int[4]
			{
				-1,
				-1,
				-1,
				0
			});
			textBoxNoofBOLs.MinValue = new decimal(new int[4]
			{
				-1,
				-1,
				-1,
				-2147483648
			});
			textBoxNoofBOLs.Name = "textBoxNoofBOLs";
			textBoxNoofBOLs.NullText = "0";
			textBoxNoofBOLs.Size = new System.Drawing.Size(55, 20);
			textBoxNoofBOLs.TabIndex = 3;
			textBoxNoofBOLs.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
			label18.AutoSize = true;
			label18.Location = new System.Drawing.Point(4, 28);
			label18.Name = "label18";
			label18.Size = new System.Drawing.Size(41, 13);
			label18.TabIndex = 212;
			label18.Text = "Goods:";
			label17.AutoSize = true;
			label17.Location = new System.Drawing.Point(5, 52);
			label17.Name = "label17";
			label17.Size = new System.Drawing.Size(55, 13);
			label17.TabIndex = 211;
			label17.Text = "No: of PL:";
			label16.AutoSize = true;
			label16.Location = new System.Drawing.Point(248, 6);
			label16.Name = "label16";
			label16.Size = new System.Drawing.Size(63, 13);
			label16.TabIndex = 210;
			label16.Text = "No: of BOL:";
			textBoxNoofInvoices.AllowDecimal = true;
			textBoxNoofInvoices.CustomReportFieldName = "";
			textBoxNoofInvoices.CustomReportKey = "";
			textBoxNoofInvoices.CustomReportValueType = 1;
			textBoxNoofInvoices.IsComboTextBox = false;
			textBoxNoofInvoices.IsModified = false;
			textBoxNoofInvoices.Location = new System.Drawing.Point(317, 26);
			textBoxNoofInvoices.MaxLength = 7;
			textBoxNoofInvoices.MaxValue = new decimal(new int[4]
			{
				-1,
				-1,
				-1,
				0
			});
			textBoxNoofInvoices.MinValue = new decimal(new int[4]
			{
				-1,
				-1,
				-1,
				-2147483648
			});
			textBoxNoofInvoices.Name = "textBoxNoofInvoices";
			textBoxNoofInvoices.NullText = "0";
			textBoxNoofInvoices.Size = new System.Drawing.Size(56, 20);
			textBoxNoofInvoices.TabIndex = 4;
			textBoxNoofInvoices.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
			label15.AutoSize = true;
			label15.Location = new System.Drawing.Point(4, 6);
			label15.Name = "label15";
			label15.Size = new System.Drawing.Size(74, 13);
			label15.TabIndex = 209;
			label15.Text = "Authorized by:";
			label14.AutoSize = true;
			label14.Location = new System.Drawing.Point(248, 29);
			label14.Name = "label14";
			label14.Size = new System.Drawing.Size(62, 13);
			label14.TabIndex = 208;
			label14.Text = "No: of Invs:";
			textBoxAuthorizedby.Location = new System.Drawing.Point(90, 2);
			textBoxAuthorizedby.MaxLength = 30;
			textBoxAuthorizedby.Name = "textBoxAuthorizedby";
			textBoxAuthorizedby.Size = new System.Drawing.Size(142, 20);
			textBoxAuthorizedby.TabIndex = 0;
			comboBoxReason.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
			comboBoxReason.FormattingEnabled = true;
			comboBoxReason.Items.AddRange(new object[2]
			{
				"Advance",
				"Outstanding Balance"
			});
			comboBoxReason.Location = new System.Drawing.Point(97, 4);
			comboBoxReason.Name = "comboBoxReason";
			comboBoxReason.Size = new System.Drawing.Size(128, 21);
			comboBoxReason.TabIndex = 1;
			label2.AutoSize = true;
			label2.Location = new System.Drawing.Point(10, 8);
			label2.Name = "label2";
			label2.Size = new System.Drawing.Size(49, 13);
			label2.TabIndex = 152;
			label2.Text = "Purpose:";
			panelButtons.Controls.Add(buttonVoid);
			panelButtons.Controls.Add(buttonDelete);
			panelButtons.Controls.Add(buttonNew);
			panelButtons.Controls.Add(linePanelDown);
			panelButtons.Controls.Add(xpButton1);
			panelButtons.Controls.Add(buttonSave);
			panelButtons.Dock = System.Windows.Forms.DockStyle.Bottom;
			panelButtons.Location = new System.Drawing.Point(0, 347);
			panelButtons.Name = "panelButtons";
			panelButtons.Size = new System.Drawing.Size(664, 40);
			panelButtons.TabIndex = 21;
			buttonVoid.AdjustImageLocation = new System.Drawing.Point(0, 0);
			buttonVoid.BackColor = System.Drawing.Color.DarkGray;
			buttonVoid.BtnShape = Micromind.UISupport.BtnShape.Rectangle;
			buttonVoid.BtnStyle = Micromind.UISupport.XPStyle.Default;
			buttonVoid.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
			buttonVoid.ImeMode = System.Windows.Forms.ImeMode.NoControl;
			buttonVoid.Location = new System.Drawing.Point(216, 8);
			buttonVoid.Name = "buttonVoid";
			buttonVoid.Size = new System.Drawing.Size(96, 24);
			buttonVoid.TabIndex = 2;
			buttonVoid.Text = "&Void";
			buttonVoid.UseVisualStyleBackColor = false;
			buttonVoid.Click += new System.EventHandler(buttonVoid_Click);
			buttonDelete.AdjustImageLocation = new System.Drawing.Point(0, 0);
			buttonDelete.BackColor = System.Drawing.Color.DarkGray;
			buttonDelete.BtnShape = Micromind.UISupport.BtnShape.Rectangle;
			buttonDelete.BtnStyle = Micromind.UISupport.XPStyle.Default;
			buttonDelete.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
			buttonDelete.ImeMode = System.Windows.Forms.ImeMode.NoControl;
			buttonDelete.Location = new System.Drawing.Point(318, 8);
			buttonDelete.Name = "buttonDelete";
			buttonDelete.Size = new System.Drawing.Size(96, 24);
			buttonDelete.TabIndex = 3;
			buttonDelete.Text = "De&lete";
			buttonDelete.UseVisualStyleBackColor = false;
			buttonDelete.Click += new System.EventHandler(buttonDelete_Click);
			buttonNew.AdjustImageLocation = new System.Drawing.Point(0, 0);
			buttonNew.BackColor = System.Drawing.Color.DarkGray;
			buttonNew.BtnShape = Micromind.UISupport.BtnShape.Rectangle;
			buttonNew.BtnStyle = Micromind.UISupport.XPStyle.Default;
			buttonNew.ImeMode = System.Windows.Forms.ImeMode.NoControl;
			buttonNew.Location = new System.Drawing.Point(114, 8);
			buttonNew.Name = "buttonNew";
			buttonNew.Size = new System.Drawing.Size(96, 24);
			buttonNew.TabIndex = 1;
			buttonNew.Text = "Ne&w...";
			buttonNew.UseVisualStyleBackColor = false;
			buttonNew.Click += new System.EventHandler(buttonNew_Click);
			linePanelDown.BackColor = System.Drawing.Color.White;
			linePanelDown.Dock = System.Windows.Forms.DockStyle.Top;
			linePanelDown.DrawWidth = 1;
			linePanelDown.IsVertical = false;
			linePanelDown.LineBackColor = System.Drawing.Color.Silver;
			linePanelDown.Location = new System.Drawing.Point(0, 0);
			linePanelDown.Name = "linePanelDown";
			linePanelDown.Size = new System.Drawing.Size(664, 1);
			linePanelDown.TabIndex = 0;
			linePanelDown.TabStop = false;
			xpButton1.AdjustImageLocation = new System.Drawing.Point(0, 0);
			xpButton1.Anchor = (System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right);
			xpButton1.BackColor = System.Drawing.Color.DarkGray;
			xpButton1.BtnShape = Micromind.UISupport.BtnShape.Rectangle;
			xpButton1.BtnStyle = Micromind.UISupport.XPStyle.Default;
			xpButton1.DialogResult = System.Windows.Forms.DialogResult.Cancel;
			xpButton1.ImeMode = System.Windows.Forms.ImeMode.NoControl;
			xpButton1.Location = new System.Drawing.Point(554, 8);
			xpButton1.Name = "xpButton1";
			xpButton1.Size = new System.Drawing.Size(96, 24);
			xpButton1.TabIndex = 4;
			xpButton1.Text = "&Close";
			xpButton1.UseVisualStyleBackColor = false;
			xpButton1.Click += new System.EventHandler(xpButton1_Click);
			buttonSave.AdjustImageLocation = new System.Drawing.Point(0, 0);
			buttonSave.BackColor = System.Drawing.Color.Silver;
			buttonSave.BtnShape = Micromind.UISupport.BtnShape.Rectangle;
			buttonSave.BtnStyle = Micromind.UISupport.XPStyle.Default;
			buttonSave.DialogResult = System.Windows.Forms.DialogResult.Cancel;
			buttonSave.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
			buttonSave.ImeMode = System.Windows.Forms.ImeMode.NoControl;
			buttonSave.Location = new System.Drawing.Point(12, 8);
			buttonSave.Name = "buttonSave";
			buttonSave.Size = new System.Drawing.Size(96, 24);
			buttonSave.TabIndex = 0;
			buttonSave.Text = "&Save";
			buttonSave.UseVisualStyleBackColor = false;
			buttonSave.Click += new System.EventHandler(buttonSave_Click);
			contextMenuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[6]
			{
				availableQuantityToolStripMenuItem,
				salesStatisticsToolStripMenuItem,
				itemPicToolStripMenuItem,
				itemDetailsToolStripMenuItem,
				toolStripSeparator3,
				removeRowToolStripMenuItem
			});
			contextMenuStrip1.Name = "contextMenuStrip1";
			contextMenuStrip1.Size = new System.Drawing.Size(181, 120);
			availableQuantityToolStripMenuItem.Name = "availableQuantityToolStripMenuItem";
			availableQuantityToolStripMenuItem.Size = new System.Drawing.Size(180, 22);
			availableQuantityToolStripMenuItem.Text = "Available Quantity...";
			salesStatisticsToolStripMenuItem.Name = "salesStatisticsToolStripMenuItem";
			salesStatisticsToolStripMenuItem.Size = new System.Drawing.Size(180, 22);
			salesStatisticsToolStripMenuItem.Text = "Sales Statistics...";
			itemPicToolStripMenuItem.Name = "itemPicToolStripMenuItem";
			itemPicToolStripMenuItem.Size = new System.Drawing.Size(180, 22);
			itemPicToolStripMenuItem.Text = "Item Photo...";
			itemDetailsToolStripMenuItem.Name = "itemDetailsToolStripMenuItem";
			itemDetailsToolStripMenuItem.Size = new System.Drawing.Size(180, 22);
			itemDetailsToolStripMenuItem.Text = "Item Details...";
			toolStripSeparator3.Name = "toolStripSeparator3";
			toolStripSeparator3.Size = new System.Drawing.Size(177, 6);
			removeRowToolStripMenuItem.Image = Micromind.ClientUI.Properties.Resources.Delete;
			removeRowToolStripMenuItem.Name = "removeRowToolStripMenuItem";
			removeRowToolStripMenuItem.Size = new System.Drawing.Size(180, 22);
			removeRowToolStripMenuItem.Text = "Remove Row";
			panelDetails.Controls.Add(textBoxTotalQualityClaim);
			panelDetails.Controls.Add(textBoxTotalPurchaseClaim);
			panelDetails.Controls.Add(linklabelPC);
			panelDetails.Controls.Add(linklabelQC);
			panelDetails.Controls.Add(mmLabel6);
			panelDetails.Controls.Add(mmLabel3);
			panelDetails.Controls.Add(label10);
			panelDetails.Controls.Add(mmLabel4);
			panelDetails.Controls.Add(textBoxTotalDue);
			panelDetails.Controls.Add(labelVendorBalance);
			panelDetails.Controls.Add(textBoxTotalBalance);
			panelDetails.Controls.Add(textBoxTerm);
			panelDetails.Controls.Add(buttonSelectRequest);
			panelDetails.Controls.Add(ultraFormattedLinkLabel1);
			panelDetails.Controls.Add(textBoxRequest);
			panelDetails.Controls.Add(ultraFormattedLinkLabel5);
			panelDetails.Controls.Add(comboBoxVendor);
			panelDetails.Controls.Add(mmLabel1);
			panelDetails.Controls.Add(label1);
			panelDetails.Controls.Add(currencySelector);
			panelDetails.Controls.Add(textBoxDescription);
			panelDetails.Controls.Add(textBoxTRNote);
			panelDetails.Controls.Add(label4);
			panelDetails.Controls.Add(labelCurrency);
			panelDetails.Controls.Add(ultraFormattedLinkLabel2);
			panelDetails.Controls.Add(ultraFormattedLinkLabel3);
			panelDetails.Controls.Add(dateTimePickerDate);
			panelDetails.Controls.Add(textBoxVoucherNumber);
			panelDetails.Controls.Add(comboBoxCostCenter);
			panelDetails.Controls.Add(textBoxPayeeName);
			panelDetails.Controls.Add(ultraFormattedLinkLabel6);
			panelDetails.Controls.Add(comboBoxSysDoc);
			panelDetails.Controls.Add(comboBoxVendorTerm);
			panelDetails.Location = new System.Drawing.Point(3, 34);
			panelDetails.Name = "panelDetails";
			panelDetails.Size = new System.Drawing.Size(650, 169);
			panelDetails.TabIndex = 0;
			textBoxTotalQualityClaim.AutoSize = true;
			textBoxTotalQualityClaim.Location = new System.Drawing.Point(106, 101);
			textBoxTotalQualityClaim.Name = "textBoxTotalQualityClaim";
			textBoxTotalQualityClaim.Size = new System.Drawing.Size(22, 13);
			textBoxTotalQualityClaim.TabIndex = 13;
			textBoxTotalQualityClaim.Text = "0.0";
			textBoxTotalQualityClaim.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
			textBoxTotalPurchaseClaim.AutoSize = true;
			textBoxTotalPurchaseClaim.Location = new System.Drawing.Point(324, 101);
			textBoxTotalPurchaseClaim.Name = "textBoxTotalPurchaseClaim";
			textBoxTotalPurchaseClaim.Size = new System.Drawing.Size(22, 13);
			textBoxTotalPurchaseClaim.TabIndex = 16;
			textBoxTotalPurchaseClaim.Text = "0.0";
			textBoxTotalPurchaseClaim.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
			linklabelPC.AutoSize = true;
			linklabelPC.AvailableInEdition = true;
			linklabelPC.Description = "";
			linklabelPC.LinkArea = new System.Windows.Forms.LinkArea(0, 53);
			linklabelPC.Location = new System.Drawing.Point(372, 102);
			linklabelPC.Name = "linklabelPC";
			linklabelPC.OriginalText = "";
			linklabelPC.Size = new System.Drawing.Size(19, 17);
			linklabelPC.TabIndex = 229;
			linklabelPC.TabStop = true;
			linklabelPC.Text = "bl2";
			linklabelPC.ToBeAligned = true;
			linklabelPC.UseCompatibleTextRendering = true;
			linklabelPC.LinkClicked += new System.Windows.Forms.LinkLabelLinkClickedEventHandler(linklabelPC_LinkClicked);
			linklabelQC.AutoSize = true;
			linklabelQC.AvailableInEdition = true;
			linklabelQC.Description = "";
			linklabelQC.LinkArea = new System.Windows.Forms.LinkArea(0, 53);
			linklabelQC.Location = new System.Drawing.Point(163, 102);
			linklabelQC.Name = "linklabelQC";
			linklabelQC.OriginalText = "";
			linklabelQC.Size = new System.Drawing.Size(19, 17);
			linklabelQC.TabIndex = 14;
			linklabelQC.TabStop = true;
			linklabelQC.Text = "bl1";
			linklabelQC.ToBeAligned = true;
			linklabelQC.UseCompatibleTextRendering = true;
			linklabelQC.LinkClicked += new System.Windows.Forms.LinkLabelLinkClickedEventHandler(linklabelQC_LinkClicked);
			mmLabel6.AutoSize = true;
			mmLabel6.BorderColor = System.Drawing.Color.FromArgb(78, 122, 171);
			mmLabel6.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25f);
			mmLabel6.IsFieldHeader = false;
			mmLabel6.IsRequired = false;
			mmLabel6.Location = new System.Drawing.Point(11, 102);
			mmLabel6.Name = "mmLabel6";
			mmLabel6.PenWidth = 1f;
			mmLabel6.ShowBorder = false;
			mmLabel6.Size = new System.Drawing.Size(70, 13);
			mmLabel6.TabIndex = 227;
			mmLabel6.Text = "Quality Claim:";
			mmLabel3.AutoSize = true;
			mmLabel3.BorderColor = System.Drawing.Color.FromArgb(78, 122, 171);
			mmLabel3.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25f);
			mmLabel3.IsFieldHeader = false;
			mmLabel3.IsRequired = false;
			mmLabel3.Location = new System.Drawing.Point(232, 101);
			mmLabel3.Name = "mmLabel3";
			mmLabel3.PenWidth = 1f;
			mmLabel3.ShowBorder = false;
			mmLabel3.Size = new System.Drawing.Size(83, 13);
			mmLabel3.TabIndex = 15;
			mmLabel3.Text = "Purchase Claim:";
			label10.AutoSize = true;
			label10.Location = new System.Drawing.Point(443, 79);
			label10.Name = "label10";
			label10.Size = new System.Drawing.Size(34, 13);
			label10.TabIndex = 225;
			label10.Text = "Term:";
			mmLabel4.AutoSize = true;
			mmLabel4.BorderColor = System.Drawing.Color.FromArgb(78, 122, 171);
			mmLabel4.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25f);
			mmLabel4.IsFieldHeader = false;
			mmLabel4.IsRequired = false;
			mmLabel4.Location = new System.Drawing.Point(232, 79);
			mmLabel4.Name = "mmLabel4";
			mmLabel4.PenWidth = 1f;
			mmLabel4.ShowBorder = false;
			mmLabel4.Size = new System.Drawing.Size(67, 13);
			mmLabel4.TabIndex = 223;
			mmLabel4.Text = "Current Due:";
			textBoxTotalDue.AllowDecimal = true;
			textBoxTotalDue.BackColor = System.Drawing.Color.WhiteSmoke;
			textBoxTotalDue.CustomReportFieldName = "";
			textBoxTotalDue.CustomReportKey = "";
			textBoxTotalDue.CustomReportValueType = 1;
			textBoxTotalDue.IsComboTextBox = false;
			textBoxTotalDue.IsModified = false;
			textBoxTotalDue.Location = new System.Drawing.Point(313, 75);
			textBoxTotalDue.MaxLength = 15;
			textBoxTotalDue.MaxValue = new decimal(new int[4]
			{
				-1,
				-1,
				-1,
				0
			});
			textBoxTotalDue.MinValue = new decimal(new int[4]
			{
				-1,
				-1,
				-1,
				-2147483648
			});
			textBoxTotalDue.Name = "textBoxTotalDue";
			textBoxTotalDue.NullText = "0";
			textBoxTotalDue.ReadOnly = true;
			textBoxTotalDue.Size = new System.Drawing.Size(129, 20);
			textBoxTotalDue.TabIndex = 11;
			textBoxTotalDue.Text = "0.00";
			textBoxTotalDue.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
			textBoxTotalDue.Value = new decimal(new int[4]
			{
				0,
				0,
				0,
				131072
			});
			labelVendorBalance.AutoSize = true;
			labelVendorBalance.BorderColor = System.Drawing.Color.FromArgb(78, 122, 171);
			labelVendorBalance.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25f);
			labelVendorBalance.IsFieldHeader = false;
			labelVendorBalance.IsRequired = false;
			labelVendorBalance.Location = new System.Drawing.Point(11, 78);
			labelVendorBalance.Name = "labelVendorBalance";
			labelVendorBalance.PenWidth = 1f;
			labelVendorBalance.ShowBorder = false;
			labelVendorBalance.Size = new System.Drawing.Size(86, 13);
			labelVendorBalance.TabIndex = 222;
			labelVendorBalance.Text = "Current Balance:";
			textBoxTotalBalance.AllowDecimal = true;
			textBoxTotalBalance.BackColor = System.Drawing.Color.WhiteSmoke;
			textBoxTotalBalance.CustomReportFieldName = "";
			textBoxTotalBalance.CustomReportKey = "";
			textBoxTotalBalance.CustomReportValueType = 1;
			textBoxTotalBalance.IsComboTextBox = false;
			textBoxTotalBalance.IsModified = false;
			textBoxTotalBalance.Location = new System.Drawing.Point(97, 75);
			textBoxTotalBalance.MaxLength = 15;
			textBoxTotalBalance.MaxValue = new decimal(new int[4]
			{
				-1,
				-1,
				-1,
				0
			});
			textBoxTotalBalance.MinValue = new decimal(new int[4]
			{
				-1,
				-1,
				-1,
				-2147483648
			});
			textBoxTotalBalance.Name = "textBoxTotalBalance";
			textBoxTotalBalance.NullText = "0";
			textBoxTotalBalance.ReadOnly = true;
			textBoxTotalBalance.Size = new System.Drawing.Size(129, 20);
			textBoxTotalBalance.TabIndex = 10;
			textBoxTotalBalance.Text = "0.00";
			textBoxTotalBalance.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
			textBoxTotalBalance.Value = new decimal(new int[4]
			{
				0,
				0,
				0,
				131072
			});
			textBoxTerm.BackColor = System.Drawing.Color.WhiteSmoke;
			textBoxTerm.Location = new System.Drawing.Point(483, 76);
			textBoxTerm.Name = "textBoxTerm";
			textBoxTerm.ReadOnly = true;
			textBoxTerm.Size = new System.Drawing.Size(129, 20);
			textBoxTerm.TabIndex = 12;
			textBoxTerm.TabStop = false;
			buttonSelectRequest.AdjustImageLocation = new System.Drawing.Point(0, 0);
			buttonSelectRequest.BackColor = System.Drawing.Color.DarkGray;
			buttonSelectRequest.BtnShape = Micromind.UISupport.BtnShape.Rectangle;
			buttonSelectRequest.BtnStyle = Micromind.UISupport.XPStyle.Default;
			buttonSelectRequest.ImeMode = System.Windows.Forms.ImeMode.NoControl;
			buttonSelectRequest.Location = new System.Drawing.Point(609, 5);
			buttonSelectRequest.Name = "buttonSelectRequest";
			buttonSelectRequest.Size = new System.Drawing.Size(26, 22);
			buttonSelectRequest.TabIndex = 4;
			buttonSelectRequest.Text = "...";
			buttonSelectRequest.UseVisualStyleBackColor = false;
			buttonSelectRequest.Click += new System.EventHandler(buttonSelectRequest_Click);
			appearance5.FontData.BoldAsString = "False";
			appearance5.FontData.Name = "Tahoma";
			ultraFormattedLinkLabel1.Appearance = appearance5;
			ultraFormattedLinkLabel1.AutoSize = true;
			ultraFormattedLinkLabel1.Location = new System.Drawing.Point(436, 9);
			ultraFormattedLinkLabel1.Name = "ultraFormattedLinkLabel1";
			ultraFormattedLinkLabel1.Size = new System.Drawing.Size(48, 15);
			ultraFormattedLinkLabel1.TabIndex = 129;
			ultraFormattedLinkLabel1.TabStop = true;
			ultraFormattedLinkLabel1.TreatValueAs = Infragistics.Win.FormattedLinkLabel.TreatValueAs.URL;
			ultraFormattedLinkLabel1.UnderlineLinks = Infragistics.Win.FormattedLinkLabel.UnderlineLink.WhenHovered;
			ultraFormattedLinkLabel1.Value = "Request:";
			appearance6.ForeColor = System.Drawing.Color.Blue;
			ultraFormattedLinkLabel1.VisitedLinkAppearance = appearance6;
			textBoxRequest.BackColor = System.Drawing.Color.WhiteSmoke;
			textBoxRequest.Location = new System.Drawing.Point(498, 7);
			textBoxRequest.Name = "textBoxRequest";
			textBoxRequest.ReadOnly = true;
			textBoxRequest.Size = new System.Drawing.Size(108, 20);
			textBoxRequest.TabIndex = 3;
			textBoxRequest.TabStop = false;
			appearance7.FontData.BoldAsString = "True";
			appearance7.FontData.Name = "Tahoma";
			ultraFormattedLinkLabel5.Appearance = appearance7;
			ultraFormattedLinkLabel5.AutoSize = true;
			ultraFormattedLinkLabel5.Location = new System.Drawing.Point(11, 9);
			ultraFormattedLinkLabel5.Name = "ultraFormattedLinkLabel5";
			ultraFormattedLinkLabel5.Size = new System.Drawing.Size(45, 15);
			ultraFormattedLinkLabel5.TabIndex = 116;
			ultraFormattedLinkLabel5.TabStop = true;
			ultraFormattedLinkLabel5.TreatValueAs = Infragistics.Win.FormattedLinkLabel.TreatValueAs.URL;
			ultraFormattedLinkLabel5.UnderlineLinks = Infragistics.Win.FormattedLinkLabel.UnderlineLink.WhenHovered;
			ultraFormattedLinkLabel5.Value = "Doc ID:";
			appearance8.ForeColor = System.Drawing.Color.Blue;
			ultraFormattedLinkLabel5.VisitedLinkAppearance = appearance8;
			ultraFormattedLinkLabel5.LinkClicked += new Infragistics.Win.FormattedLinkLabel.LinkClickedEventHandler(ultraFormattedLinkLabel5_LinkClicked);
			comboBoxVendor.Assigned = false;
			comboBoxVendor.AutoCompleteMode = Infragistics.Win.AutoCompleteMode.Append;
			comboBoxVendor.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper;
			comboBoxVendor.CustomReportFieldName = "";
			comboBoxVendor.CustomReportKey = "";
			comboBoxVendor.CustomReportValueType = 1;
			comboBoxVendor.DescriptionTextBox = null;
			appearance9.BackColor = System.Drawing.SystemColors.Window;
			appearance9.BorderColor = System.Drawing.SystemColors.InactiveCaption;
			comboBoxVendor.DisplayLayout.Appearance = appearance9;
			comboBoxVendor.DisplayLayout.BorderStyle = Infragistics.Win.UIElementBorderStyle.Solid;
			comboBoxVendor.DisplayLayout.CaptionVisible = Infragistics.Win.DefaultableBoolean.False;
			appearance10.BackColor = System.Drawing.SystemColors.ActiveBorder;
			appearance10.BackColor2 = System.Drawing.SystemColors.ControlDark;
			appearance10.BackGradientStyle = Infragistics.Win.GradientStyle.Vertical;
			appearance10.BorderColor = System.Drawing.SystemColors.Window;
			comboBoxVendor.DisplayLayout.GroupByBox.Appearance = appearance10;
			appearance11.ForeColor = System.Drawing.SystemColors.GrayText;
			comboBoxVendor.DisplayLayout.GroupByBox.BandLabelAppearance = appearance11;
			comboBoxVendor.DisplayLayout.GroupByBox.BorderStyle = Infragistics.Win.UIElementBorderStyle.Solid;
			appearance12.BackColor = System.Drawing.SystemColors.ControlLightLight;
			appearance12.BackColor2 = System.Drawing.SystemColors.Control;
			appearance12.BackGradientStyle = Infragistics.Win.GradientStyle.Horizontal;
			appearance12.ForeColor = System.Drawing.SystemColors.GrayText;
			comboBoxVendor.DisplayLayout.GroupByBox.PromptAppearance = appearance12;
			comboBoxVendor.DisplayLayout.MaxColScrollRegions = 1;
			comboBoxVendor.DisplayLayout.MaxRowScrollRegions = 1;
			appearance13.BackColor = System.Drawing.SystemColors.Window;
			appearance13.ForeColor = System.Drawing.SystemColors.ControlText;
			comboBoxVendor.DisplayLayout.Override.ActiveCellAppearance = appearance13;
			appearance14.BackColor = System.Drawing.SystemColors.Highlight;
			appearance14.ForeColor = System.Drawing.SystemColors.HighlightText;
			comboBoxVendor.DisplayLayout.Override.ActiveRowAppearance = appearance14;
			comboBoxVendor.DisplayLayout.Override.BorderStyleCell = Infragistics.Win.UIElementBorderStyle.Dotted;
			comboBoxVendor.DisplayLayout.Override.BorderStyleRow = Infragistics.Win.UIElementBorderStyle.Dotted;
			appearance15.BackColor = System.Drawing.SystemColors.Window;
			comboBoxVendor.DisplayLayout.Override.CardAreaAppearance = appearance15;
			appearance16.BorderColor = System.Drawing.Color.Silver;
			appearance16.TextTrimming = Infragistics.Win.TextTrimming.EllipsisCharacter;
			comboBoxVendor.DisplayLayout.Override.CellAppearance = appearance16;
			comboBoxVendor.DisplayLayout.Override.CellClickAction = Infragistics.Win.UltraWinGrid.CellClickAction.EditAndSelectText;
			comboBoxVendor.DisplayLayout.Override.CellPadding = 0;
			appearance17.BackColor = System.Drawing.SystemColors.Control;
			appearance17.BackColor2 = System.Drawing.SystemColors.ControlDark;
			appearance17.BackGradientAlignment = Infragistics.Win.GradientAlignment.Element;
			appearance17.BackGradientStyle = Infragistics.Win.GradientStyle.Horizontal;
			appearance17.BorderColor = System.Drawing.SystemColors.Window;
			comboBoxVendor.DisplayLayout.Override.GroupByRowAppearance = appearance17;
			appearance18.TextHAlignAsString = "Left";
			comboBoxVendor.DisplayLayout.Override.HeaderAppearance = appearance18;
			comboBoxVendor.DisplayLayout.Override.HeaderClickAction = Infragistics.Win.UltraWinGrid.HeaderClickAction.SortMulti;
			comboBoxVendor.DisplayLayout.Override.HeaderStyle = Infragistics.Win.HeaderStyle.WindowsXPCommand;
			appearance19.BackColor = System.Drawing.SystemColors.Window;
			appearance19.BorderColor = System.Drawing.Color.Silver;
			comboBoxVendor.DisplayLayout.Override.RowAppearance = appearance19;
			comboBoxVendor.DisplayLayout.Override.RowSelectors = Infragistics.Win.DefaultableBoolean.False;
			appearance20.BackColor = System.Drawing.SystemColors.ControlLight;
			comboBoxVendor.DisplayLayout.Override.TemplateAddRowAppearance = appearance20;
			comboBoxVendor.DisplayLayout.ScrollBounds = Infragistics.Win.UltraWinGrid.ScrollBounds.ScrollToFill;
			comboBoxVendor.DisplayLayout.ScrollStyle = Infragistics.Win.UltraWinGrid.ScrollStyle.Immediate;
			comboBoxVendor.DisplayLayout.ViewStyleBand = Infragistics.Win.UltraWinGrid.ViewStyleBand.OutlookGroupBy;
			comboBoxVendor.DropDownSearchMethod = Infragistics.Win.UltraWinGrid.DropDownSearchMethod.Linear;
			comboBoxVendor.Editable = true;
			comboBoxVendor.FilterString = "";
			comboBoxVendor.FilterSysDocID = "";
			comboBoxVendor.HasAll = false;
			comboBoxVendor.HasCustom = false;
			comboBoxVendor.IsDataLoaded = false;
			comboBoxVendor.Location = new System.Drawing.Point(97, 52);
			comboBoxVendor.MaxDropDownItems = 12;
			comboBoxVendor.Name = "comboBoxVendor";
			comboBoxVendor.ShowConsignmentOnly = false;
			comboBoxVendor.ShowQuickAdd = true;
			comboBoxVendor.Size = new System.Drawing.Size(179, 20);
			comboBoxVendor.TabIndex = 8;
			comboBoxVendor.UseFlatMode = Infragistics.Win.DefaultableBoolean.True;
			mmLabel1.AutoSize = true;
			mmLabel1.BorderColor = System.Drawing.Color.FromArgb(78, 122, 171);
			mmLabel1.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25f, System.Drawing.FontStyle.Bold);
			mmLabel1.IsFieldHeader = false;
			mmLabel1.IsRequired = true;
			mmLabel1.Location = new System.Drawing.Point(450, 32);
			mmLabel1.Name = "mmLabel1";
			mmLabel1.PenWidth = 1f;
			mmLabel1.ShowBorder = false;
			mmLabel1.Size = new System.Drawing.Size(38, 13);
			mmLabel1.TabIndex = 2;
			mmLabel1.Text = "Date:";
			label1.AutoSize = true;
			label1.Location = new System.Drawing.Point(11, 147);
			label1.Name = "label1";
			label1.Size = new System.Drawing.Size(33, 13);
			label1.TabIndex = 20;
			label1.Text = "Note:";
			currencySelector.BackColor = System.Drawing.Color.WhiteSmoke;
			currencySelector.Location = new System.Drawing.Point(270, 29);
			currencySelector.MaximumSize = new System.Drawing.Size(99999, 20);
			currencySelector.MinimumSize = new System.Drawing.Size(5, 20);
			currencySelector.Name = "currencySelector";
			currencySelector.Rate = new decimal(new int[4]
			{
				1,
				0,
				0,
				0
			});
			currencySelector.SelectedID = "";
			currencySelector.Size = new System.Drawing.Size(174, 20);
			currencySelector.TabIndex = 6;
			textBoxDescription.Location = new System.Drawing.Point(97, 122);
			textBoxDescription.MaxLength = 255;
			textBoxDescription.Name = "textBoxDescription";
			textBoxDescription.Size = new System.Drawing.Size(534, 20);
			textBoxDescription.TabIndex = 17;
			textBoxTRNote.Location = new System.Drawing.Point(97, 144);
			textBoxTRNote.MaxLength = 255;
			textBoxTRNote.Name = "textBoxTRNote";
			textBoxTRNote.Size = new System.Drawing.Size(534, 20);
			textBoxTRNote.TabIndex = 18;
			label4.AutoSize = true;
			label4.Location = new System.Drawing.Point(11, 125);
			label4.Name = "label4";
			label4.Size = new System.Drawing.Size(49, 13);
			label4.TabIndex = 127;
			label4.Text = "Paid For:";
			appearance21.FontData.BoldAsString = "False";
			labelCurrency.Appearance = appearance21;
			labelCurrency.AutoSize = true;
			labelCurrency.Location = new System.Drawing.Point(215, 32);
			labelCurrency.Name = "labelCurrency";
			labelCurrency.Size = new System.Drawing.Size(52, 14);
			labelCurrency.TabIndex = 4;
			labelCurrency.TabStop = true;
			labelCurrency.TreatValueAs = Infragistics.Win.FormattedLinkLabel.TreatValueAs.URL;
			labelCurrency.UnderlineLinks = Infragistics.Win.FormattedLinkLabel.UnderlineLink.WhenHovered;
			labelCurrency.Value = "Currency:";
			appearance22.ForeColor = System.Drawing.Color.Blue;
			labelCurrency.VisitedLinkAppearance = appearance22;
			appearance23.FontData.BoldAsString = "True";
			appearance23.FontData.Name = "Tahoma";
			ultraFormattedLinkLabel2.Appearance = appearance23;
			ultraFormattedLinkLabel2.AutoSize = true;
			ultraFormattedLinkLabel2.Location = new System.Drawing.Point(213, 9);
			ultraFormattedLinkLabel2.Name = "ultraFormattedLinkLabel2";
			ultraFormattedLinkLabel2.Size = new System.Drawing.Size(101, 15);
			ultraFormattedLinkLabel2.TabIndex = 1;
			ultraFormattedLinkLabel2.TabStop = true;
			ultraFormattedLinkLabel2.TreatValueAs = Infragistics.Win.FormattedLinkLabel.TreatValueAs.URL;
			ultraFormattedLinkLabel2.UnderlineLinks = Infragistics.Win.FormattedLinkLabel.UnderlineLink.WhenHovered;
			ultraFormattedLinkLabel2.Value = "Voucher Number:";
			appearance24.ForeColor = System.Drawing.Color.Blue;
			ultraFormattedLinkLabel2.VisitedLinkAppearance = appearance24;
			ultraFormattedLinkLabel2.LinkClicked += new Infragistics.Win.FormattedLinkLabel.LinkClickedEventHandler(ultraFormattedLinkLabel2_LinkClicked);
			appearance25.FontData.BoldAsString = "True";
			appearance25.FontData.Name = "Tahoma";
			ultraFormattedLinkLabel3.Appearance = appearance25;
			ultraFormattedLinkLabel3.AutoSize = true;
			ultraFormattedLinkLabel3.Location = new System.Drawing.Point(11, 53);
			ultraFormattedLinkLabel3.Name = "ultraFormattedLinkLabel3";
			ultraFormattedLinkLabel3.Size = new System.Drawing.Size(48, 15);
			ultraFormattedLinkLabel3.TabIndex = 112;
			ultraFormattedLinkLabel3.TabStop = true;
			ultraFormattedLinkLabel3.TreatValueAs = Infragistics.Win.FormattedLinkLabel.TreatValueAs.URL;
			ultraFormattedLinkLabel3.UnderlineLinks = Infragistics.Win.FormattedLinkLabel.UnderlineLink.WhenHovered;
			ultraFormattedLinkLabel3.Value = "Vendor:";
			appearance26.ForeColor = System.Drawing.Color.Blue;
			ultraFormattedLinkLabel3.VisitedLinkAppearance = appearance26;
			ultraFormattedLinkLabel3.LinkClicked += new Infragistics.Win.FormattedLinkLabel.LinkClickedEventHandler(ultraFormattedLinkLabel3_LinkClicked);
			dateTimePickerDate.Format = System.Windows.Forms.DateTimePickerFormat.Short;
			dateTimePickerDate.Location = new System.Drawing.Point(498, 29);
			dateTimePickerDate.Name = "dateTimePickerDate";
			dateTimePickerDate.Size = new System.Drawing.Size(133, 20);
			dateTimePickerDate.TabIndex = 7;
			dateTimePickerDate.Value = new System.DateTime(2008, 5, 15, 11, 57, 9, 732);
			textBoxVoucherNumber.Location = new System.Drawing.Point(319, 7);
			textBoxVoucherNumber.MaxLength = 15;
			textBoxVoucherNumber.Name = "textBoxVoucherNumber";
			textBoxVoucherNumber.Size = new System.Drawing.Size(111, 20);
			textBoxVoucherNumber.TabIndex = 2;
			comboBoxCostCenter.AlwaysInEditMode = true;
			comboBoxCostCenter.Assigned = false;
			comboBoxCostCenter.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper;
			comboBoxCostCenter.CustomReportFieldName = "";
			comboBoxCostCenter.CustomReportKey = "";
			comboBoxCostCenter.CustomReportValueType = 1;
			comboBoxCostCenter.DescriptionTextBox = null;
			appearance27.BackColor = System.Drawing.SystemColors.Window;
			appearance27.BorderColor = System.Drawing.SystemColors.InactiveCaption;
			comboBoxCostCenter.DisplayLayout.Appearance = appearance27;
			comboBoxCostCenter.DisplayLayout.BorderStyle = Infragistics.Win.UIElementBorderStyle.Solid;
			comboBoxCostCenter.DisplayLayout.CaptionVisible = Infragistics.Win.DefaultableBoolean.False;
			appearance28.BackColor = System.Drawing.SystemColors.ActiveBorder;
			appearance28.BackColor2 = System.Drawing.SystemColors.ControlDark;
			appearance28.BackGradientStyle = Infragistics.Win.GradientStyle.Vertical;
			appearance28.BorderColor = System.Drawing.SystemColors.Window;
			comboBoxCostCenter.DisplayLayout.GroupByBox.Appearance = appearance28;
			appearance29.ForeColor = System.Drawing.SystemColors.GrayText;
			comboBoxCostCenter.DisplayLayout.GroupByBox.BandLabelAppearance = appearance29;
			comboBoxCostCenter.DisplayLayout.GroupByBox.BorderStyle = Infragistics.Win.UIElementBorderStyle.Solid;
			appearance30.BackColor = System.Drawing.SystemColors.ControlLightLight;
			appearance30.BackColor2 = System.Drawing.SystemColors.Control;
			appearance30.BackGradientStyle = Infragistics.Win.GradientStyle.Horizontal;
			appearance30.ForeColor = System.Drawing.SystemColors.GrayText;
			comboBoxCostCenter.DisplayLayout.GroupByBox.PromptAppearance = appearance30;
			comboBoxCostCenter.DisplayLayout.MaxColScrollRegions = 1;
			comboBoxCostCenter.DisplayLayout.MaxRowScrollRegions = 1;
			appearance31.BackColor = System.Drawing.SystemColors.Window;
			appearance31.ForeColor = System.Drawing.SystemColors.ControlText;
			comboBoxCostCenter.DisplayLayout.Override.ActiveCellAppearance = appearance31;
			appearance32.BackColor = System.Drawing.SystemColors.Highlight;
			appearance32.ForeColor = System.Drawing.SystemColors.HighlightText;
			comboBoxCostCenter.DisplayLayout.Override.ActiveRowAppearance = appearance32;
			comboBoxCostCenter.DisplayLayout.Override.BorderStyleCell = Infragistics.Win.UIElementBorderStyle.Dotted;
			comboBoxCostCenter.DisplayLayout.Override.BorderStyleRow = Infragistics.Win.UIElementBorderStyle.Dotted;
			appearance33.BackColor = System.Drawing.SystemColors.Window;
			comboBoxCostCenter.DisplayLayout.Override.CardAreaAppearance = appearance33;
			appearance34.BorderColor = System.Drawing.Color.Silver;
			appearance34.TextTrimming = Infragistics.Win.TextTrimming.EllipsisCharacter;
			comboBoxCostCenter.DisplayLayout.Override.CellAppearance = appearance34;
			comboBoxCostCenter.DisplayLayout.Override.CellClickAction = Infragistics.Win.UltraWinGrid.CellClickAction.EditAndSelectText;
			comboBoxCostCenter.DisplayLayout.Override.CellPadding = 0;
			appearance35.BackColor = System.Drawing.SystemColors.Control;
			appearance35.BackColor2 = System.Drawing.SystemColors.ControlDark;
			appearance35.BackGradientAlignment = Infragistics.Win.GradientAlignment.Element;
			appearance35.BackGradientStyle = Infragistics.Win.GradientStyle.Horizontal;
			appearance35.BorderColor = System.Drawing.SystemColors.Window;
			comboBoxCostCenter.DisplayLayout.Override.GroupByRowAppearance = appearance35;
			appearance36.TextHAlignAsString = "Left";
			comboBoxCostCenter.DisplayLayout.Override.HeaderAppearance = appearance36;
			comboBoxCostCenter.DisplayLayout.Override.HeaderClickAction = Infragistics.Win.UltraWinGrid.HeaderClickAction.SortMulti;
			comboBoxCostCenter.DisplayLayout.Override.HeaderStyle = Infragistics.Win.HeaderStyle.WindowsXPCommand;
			appearance37.BackColor = System.Drawing.SystemColors.Window;
			appearance37.BorderColor = System.Drawing.Color.Silver;
			comboBoxCostCenter.DisplayLayout.Override.RowAppearance = appearance37;
			comboBoxCostCenter.DisplayLayout.Override.RowSelectors = Infragistics.Win.DefaultableBoolean.False;
			appearance38.BackColor = System.Drawing.SystemColors.ControlLight;
			comboBoxCostCenter.DisplayLayout.Override.TemplateAddRowAppearance = appearance38;
			comboBoxCostCenter.DisplayLayout.ScrollBounds = Infragistics.Win.UltraWinGrid.ScrollBounds.ScrollToFill;
			comboBoxCostCenter.DisplayLayout.ScrollStyle = Infragistics.Win.UltraWinGrid.ScrollStyle.Immediate;
			comboBoxCostCenter.DisplayLayout.ViewStyleBand = Infragistics.Win.UltraWinGrid.ViewStyleBand.OutlookGroupBy;
			comboBoxCostCenter.DropDownSearchMethod = Infragistics.Win.UltraWinGrid.DropDownSearchMethod.Linear;
			comboBoxCostCenter.Editable = true;
			comboBoxCostCenter.FilterString = "";
			comboBoxCostCenter.HasAllAccount = false;
			comboBoxCostCenter.HasCustom = false;
			comboBoxCostCenter.IsDataLoaded = false;
			comboBoxCostCenter.Location = new System.Drawing.Point(97, 29);
			comboBoxCostCenter.MaxDropDownItems = 12;
			comboBoxCostCenter.Name = "comboBoxCostCenter";
			comboBoxCostCenter.ShowInactiveItems = false;
			comboBoxCostCenter.ShowQuickAdd = true;
			comboBoxCostCenter.Size = new System.Drawing.Size(111, 20);
			comboBoxCostCenter.TabIndex = 5;
			comboBoxCostCenter.UseFlatMode = Infragistics.Win.DefaultableBoolean.True;
			textBoxPayeeName.BackColor = System.Drawing.Color.WhiteSmoke;
			textBoxPayeeName.Location = new System.Drawing.Point(279, 52);
			textBoxPayeeName.Name = "textBoxPayeeName";
			textBoxPayeeName.ReadOnly = true;
			textBoxPayeeName.Size = new System.Drawing.Size(352, 20);
			textBoxPayeeName.TabIndex = 9;
			textBoxPayeeName.TabStop = false;
			appearance39.FontData.BoldAsString = "False";
			appearance39.FontData.Name = "Tahoma";
			ultraFormattedLinkLabel6.Appearance = appearance39;
			ultraFormattedLinkLabel6.AutoSize = true;
			ultraFormattedLinkLabel6.Location = new System.Drawing.Point(11, 29);
			ultraFormattedLinkLabel6.Name = "ultraFormattedLinkLabel6";
			ultraFormattedLinkLabel6.Size = new System.Drawing.Size(65, 15);
			ultraFormattedLinkLabel6.TabIndex = 114;
			ultraFormattedLinkLabel6.TabStop = true;
			ultraFormattedLinkLabel6.TreatValueAs = Infragistics.Win.FormattedLinkLabel.TreatValueAs.URL;
			ultraFormattedLinkLabel6.UnderlineLinks = Infragistics.Win.FormattedLinkLabel.UnderlineLink.WhenHovered;
			ultraFormattedLinkLabel6.Value = "Cost Center:";
			appearance40.ForeColor = System.Drawing.Color.Blue;
			ultraFormattedLinkLabel6.VisitedLinkAppearance = appearance40;
			comboBoxSysDoc.AlwaysInEditMode = true;
			comboBoxSysDoc.Assigned = false;
			comboBoxSysDoc.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper;
			comboBoxSysDoc.CustomReportFieldName = "";
			comboBoxSysDoc.CustomReportKey = "";
			comboBoxSysDoc.CustomReportValueType = 1;
			comboBoxSysDoc.DescriptionTextBox = null;
			appearance41.BackColor = System.Drawing.SystemColors.Window;
			appearance41.BorderColor = System.Drawing.SystemColors.InactiveCaption;
			comboBoxSysDoc.DisplayLayout.Appearance = appearance41;
			comboBoxSysDoc.DisplayLayout.BorderStyle = Infragistics.Win.UIElementBorderStyle.Solid;
			comboBoxSysDoc.DisplayLayout.CaptionVisible = Infragistics.Win.DefaultableBoolean.False;
			appearance42.BackColor = System.Drawing.SystemColors.ActiveBorder;
			appearance42.BackColor2 = System.Drawing.SystemColors.ControlDark;
			appearance42.BackGradientStyle = Infragistics.Win.GradientStyle.Vertical;
			appearance42.BorderColor = System.Drawing.SystemColors.Window;
			comboBoxSysDoc.DisplayLayout.GroupByBox.Appearance = appearance42;
			appearance43.ForeColor = System.Drawing.SystemColors.GrayText;
			comboBoxSysDoc.DisplayLayout.GroupByBox.BandLabelAppearance = appearance43;
			comboBoxSysDoc.DisplayLayout.GroupByBox.BorderStyle = Infragistics.Win.UIElementBorderStyle.Solid;
			appearance44.BackColor = System.Drawing.SystemColors.ControlLightLight;
			appearance44.BackColor2 = System.Drawing.SystemColors.Control;
			appearance44.BackGradientStyle = Infragistics.Win.GradientStyle.Horizontal;
			appearance44.ForeColor = System.Drawing.SystemColors.GrayText;
			comboBoxSysDoc.DisplayLayout.GroupByBox.PromptAppearance = appearance44;
			comboBoxSysDoc.DisplayLayout.MaxColScrollRegions = 1;
			comboBoxSysDoc.DisplayLayout.MaxRowScrollRegions = 1;
			appearance45.BackColor = System.Drawing.SystemColors.Window;
			appearance45.ForeColor = System.Drawing.SystemColors.ControlText;
			comboBoxSysDoc.DisplayLayout.Override.ActiveCellAppearance = appearance45;
			appearance46.BackColor = System.Drawing.SystemColors.Highlight;
			appearance46.ForeColor = System.Drawing.SystemColors.HighlightText;
			comboBoxSysDoc.DisplayLayout.Override.ActiveRowAppearance = appearance46;
			comboBoxSysDoc.DisplayLayout.Override.BorderStyleCell = Infragistics.Win.UIElementBorderStyle.Dotted;
			comboBoxSysDoc.DisplayLayout.Override.BorderStyleRow = Infragistics.Win.UIElementBorderStyle.Dotted;
			appearance47.BackColor = System.Drawing.SystemColors.Window;
			comboBoxSysDoc.DisplayLayout.Override.CardAreaAppearance = appearance47;
			appearance48.BorderColor = System.Drawing.Color.Silver;
			appearance48.TextTrimming = Infragistics.Win.TextTrimming.EllipsisCharacter;
			comboBoxSysDoc.DisplayLayout.Override.CellAppearance = appearance48;
			comboBoxSysDoc.DisplayLayout.Override.CellClickAction = Infragistics.Win.UltraWinGrid.CellClickAction.EditAndSelectText;
			comboBoxSysDoc.DisplayLayout.Override.CellPadding = 0;
			appearance49.BackColor = System.Drawing.SystemColors.Control;
			appearance49.BackColor2 = System.Drawing.SystemColors.ControlDark;
			appearance49.BackGradientAlignment = Infragistics.Win.GradientAlignment.Element;
			appearance49.BackGradientStyle = Infragistics.Win.GradientStyle.Horizontal;
			appearance49.BorderColor = System.Drawing.SystemColors.Window;
			comboBoxSysDoc.DisplayLayout.Override.GroupByRowAppearance = appearance49;
			appearance50.TextHAlignAsString = "Left";
			comboBoxSysDoc.DisplayLayout.Override.HeaderAppearance = appearance50;
			comboBoxSysDoc.DisplayLayout.Override.HeaderClickAction = Infragistics.Win.UltraWinGrid.HeaderClickAction.SortMulti;
			comboBoxSysDoc.DisplayLayout.Override.HeaderStyle = Infragistics.Win.HeaderStyle.WindowsXPCommand;
			appearance51.BackColor = System.Drawing.SystemColors.Window;
			appearance51.BorderColor = System.Drawing.Color.Silver;
			comboBoxSysDoc.DisplayLayout.Override.RowAppearance = appearance51;
			comboBoxSysDoc.DisplayLayout.Override.RowSelectors = Infragistics.Win.DefaultableBoolean.False;
			appearance52.BackColor = System.Drawing.SystemColors.ControlLight;
			comboBoxSysDoc.DisplayLayout.Override.TemplateAddRowAppearance = appearance52;
			comboBoxSysDoc.DisplayLayout.ScrollBounds = Infragistics.Win.UltraWinGrid.ScrollBounds.ScrollToFill;
			comboBoxSysDoc.DisplayLayout.ScrollStyle = Infragistics.Win.UltraWinGrid.ScrollStyle.Immediate;
			comboBoxSysDoc.DisplayLayout.ViewStyleBand = Infragistics.Win.UltraWinGrid.ViewStyleBand.OutlookGroupBy;
			comboBoxSysDoc.DivisionID = "";
			comboBoxSysDoc.DropDownSearchMethod = Infragistics.Win.UltraWinGrid.DropDownSearchMethod.Linear;
			comboBoxSysDoc.DropDownStyle = Infragistics.Win.UltraWinGrid.UltraComboStyle.DropDownList;
			comboBoxSysDoc.Editable = true;
			comboBoxSysDoc.ExcludeFromSecurity = false;
			comboBoxSysDoc.FilterString = "";
			comboBoxSysDoc.HasAllAccount = false;
			comboBoxSysDoc.HasCustom = false;
			comboBoxSysDoc.IsDataLoaded = false;
			comboBoxSysDoc.Location = new System.Drawing.Point(97, 7);
			comboBoxSysDoc.MaxDropDownItems = 12;
			comboBoxSysDoc.Name = "comboBoxSysDoc";
			comboBoxSysDoc.ShowAll = false;
			comboBoxSysDoc.ShowInactiveItems = false;
			comboBoxSysDoc.ShowQuickAdd = true;
			comboBoxSysDoc.Size = new System.Drawing.Size(111, 20);
			comboBoxSysDoc.TabIndex = 1;
			comboBoxSysDoc.UseFlatMode = Infragistics.Win.DefaultableBoolean.True;
			comboBoxVendorTerm.Assigned = false;
			comboBoxVendorTerm.AutoCompleteMode = Infragistics.Win.AutoCompleteMode.Append;
			comboBoxVendorTerm.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper;
			comboBoxVendorTerm.CustomReportFieldName = "";
			comboBoxVendorTerm.CustomReportKey = "";
			comboBoxVendorTerm.CustomReportValueType = 1;
			comboBoxVendorTerm.DescriptionTextBox = textBoxTerm;
			appearance53.BackColor = System.Drawing.SystemColors.Window;
			appearance53.BorderColor = System.Drawing.SystemColors.InactiveCaption;
			comboBoxVendorTerm.DisplayLayout.Appearance = appearance53;
			comboBoxVendorTerm.DisplayLayout.BorderStyle = Infragistics.Win.UIElementBorderStyle.Solid;
			comboBoxVendorTerm.DisplayLayout.CaptionVisible = Infragistics.Win.DefaultableBoolean.False;
			appearance54.BackColor = System.Drawing.SystemColors.ActiveBorder;
			appearance54.BackColor2 = System.Drawing.SystemColors.ControlDark;
			appearance54.BackGradientStyle = Infragistics.Win.GradientStyle.Vertical;
			appearance54.BorderColor = System.Drawing.SystemColors.Window;
			comboBoxVendorTerm.DisplayLayout.GroupByBox.Appearance = appearance54;
			appearance55.ForeColor = System.Drawing.SystemColors.GrayText;
			comboBoxVendorTerm.DisplayLayout.GroupByBox.BandLabelAppearance = appearance55;
			comboBoxVendorTerm.DisplayLayout.GroupByBox.BorderStyle = Infragistics.Win.UIElementBorderStyle.Solid;
			appearance56.BackColor = System.Drawing.SystemColors.ControlLightLight;
			appearance56.BackColor2 = System.Drawing.SystemColors.Control;
			appearance56.BackGradientStyle = Infragistics.Win.GradientStyle.Horizontal;
			appearance56.ForeColor = System.Drawing.SystemColors.GrayText;
			comboBoxVendorTerm.DisplayLayout.GroupByBox.PromptAppearance = appearance56;
			comboBoxVendorTerm.DisplayLayout.MaxColScrollRegions = 1;
			comboBoxVendorTerm.DisplayLayout.MaxRowScrollRegions = 1;
			appearance57.BackColor = System.Drawing.SystemColors.Window;
			appearance57.ForeColor = System.Drawing.SystemColors.ControlText;
			comboBoxVendorTerm.DisplayLayout.Override.ActiveCellAppearance = appearance57;
			appearance58.BackColor = System.Drawing.SystemColors.Highlight;
			appearance58.ForeColor = System.Drawing.SystemColors.HighlightText;
			comboBoxVendorTerm.DisplayLayout.Override.ActiveRowAppearance = appearance58;
			comboBoxVendorTerm.DisplayLayout.Override.BorderStyleCell = Infragistics.Win.UIElementBorderStyle.Dotted;
			comboBoxVendorTerm.DisplayLayout.Override.BorderStyleRow = Infragistics.Win.UIElementBorderStyle.Dotted;
			appearance59.BackColor = System.Drawing.SystemColors.Window;
			comboBoxVendorTerm.DisplayLayout.Override.CardAreaAppearance = appearance59;
			appearance60.BorderColor = System.Drawing.Color.Silver;
			appearance60.TextTrimming = Infragistics.Win.TextTrimming.EllipsisCharacter;
			comboBoxVendorTerm.DisplayLayout.Override.CellAppearance = appearance60;
			comboBoxVendorTerm.DisplayLayout.Override.CellClickAction = Infragistics.Win.UltraWinGrid.CellClickAction.EditAndSelectText;
			comboBoxVendorTerm.DisplayLayout.Override.CellPadding = 0;
			appearance61.BackColor = System.Drawing.SystemColors.Control;
			appearance61.BackColor2 = System.Drawing.SystemColors.ControlDark;
			appearance61.BackGradientAlignment = Infragistics.Win.GradientAlignment.Element;
			appearance61.BackGradientStyle = Infragistics.Win.GradientStyle.Horizontal;
			appearance61.BorderColor = System.Drawing.SystemColors.Window;
			comboBoxVendorTerm.DisplayLayout.Override.GroupByRowAppearance = appearance61;
			appearance62.TextHAlignAsString = "Left";
			comboBoxVendorTerm.DisplayLayout.Override.HeaderAppearance = appearance62;
			comboBoxVendorTerm.DisplayLayout.Override.HeaderClickAction = Infragistics.Win.UltraWinGrid.HeaderClickAction.SortMulti;
			comboBoxVendorTerm.DisplayLayout.Override.HeaderStyle = Infragistics.Win.HeaderStyle.WindowsXPCommand;
			appearance63.BackColor = System.Drawing.SystemColors.Window;
			appearance63.BorderColor = System.Drawing.Color.Silver;
			comboBoxVendorTerm.DisplayLayout.Override.RowAppearance = appearance63;
			comboBoxVendorTerm.DisplayLayout.Override.RowSelectors = Infragistics.Win.DefaultableBoolean.False;
			appearance64.BackColor = System.Drawing.SystemColors.ControlLight;
			comboBoxVendorTerm.DisplayLayout.Override.TemplateAddRowAppearance = appearance64;
			comboBoxVendorTerm.DisplayLayout.ScrollBounds = Infragistics.Win.UltraWinGrid.ScrollBounds.ScrollToFill;
			comboBoxVendorTerm.DisplayLayout.ScrollStyle = Infragistics.Win.UltraWinGrid.ScrollStyle.Immediate;
			comboBoxVendorTerm.DisplayLayout.ViewStyleBand = Infragistics.Win.UltraWinGrid.ViewStyleBand.OutlookGroupBy;
			comboBoxVendorTerm.DropDownSearchMethod = Infragistics.Win.UltraWinGrid.DropDownSearchMethod.Linear;
			comboBoxVendorTerm.Editable = true;
			comboBoxVendorTerm.FilterString = "";
			comboBoxVendorTerm.HasAllAccount = false;
			comboBoxVendorTerm.HasCustom = false;
			comboBoxVendorTerm.IsDataLoaded = false;
			comboBoxVendorTerm.Location = new System.Drawing.Point(483, 76);
			comboBoxVendorTerm.MaxDropDownItems = 12;
			comboBoxVendorTerm.Name = "comboBoxVendorTerm";
			comboBoxVendorTerm.ShowInactiveItems = false;
			comboBoxVendorTerm.ShowQuickAdd = true;
			comboBoxVendorTerm.Size = new System.Drawing.Size(100, 20);
			comboBoxVendorTerm.TabIndex = 232;
			comboBoxVendorTerm.UseFlatMode = Infragistics.Win.DefaultableBoolean.True;
			comboBoxVendorTerm.Visible = false;
			panel1.Controls.Add(panelPO);
			panel1.Controls.Add(panelTR);
			panel1.Controls.Add(comboBoxReason);
			panel1.Controls.Add(label3);
			panel1.Controls.Add(textBoxNote);
			panel1.Controls.Add(labelInvnos);
			panel1.Controls.Add(comboBoxPOTerm);
			panel1.Controls.Add(textBoxInvoiceNo);
			panel1.Controls.Add(label2);
			panel1.Location = new System.Drawing.Point(624, 267);
			panel1.Name = "panel1";
			panel1.Size = new System.Drawing.Size(10, 58);
			panel1.TabIndex = 219;
			panel1.Visible = false;
			panelPO.Controls.Add(dateTimePickerETA);
			panelPO.Controls.Add(label13);
			panelPO.Controls.Add(textBoxPOSysDocID);
			panelPO.Controls.Add(buttonSelectPO);
			panelPO.Controls.Add(textBoxPOVoucherID);
			panelPO.Controls.Add(label9);
			panelPO.Controls.Add(textBoxPOTerm);
			panelPO.Controls.Add(label8);
			panelPO.Controls.Add(textBoxPOBalance);
			panelPO.Controls.Add(label7);
			panelPO.Controls.Add(textBoxPOPaid);
			panelPO.Controls.Add(label6);
			panelPO.Controls.Add(textBoxPOAmount);
			panelPO.Controls.Add(label5);
			panelPO.Controls.Add(paymentTermComboBox1);
			panelPO.Location = new System.Drawing.Point(3, 25);
			panelPO.Name = "panelPO";
			panelPO.Size = new System.Drawing.Size(56, 50);
			panelPO.TabIndex = 213;
			dateTimePickerETA.BackColor = System.Drawing.Color.WhiteSmoke;
			dateTimePickerETA.Location = new System.Drawing.Point(488, 3);
			dateTimePickerETA.Name = "dateTimePickerETA";
			dateTimePickerETA.ReadOnly = true;
			dateTimePickerETA.Size = new System.Drawing.Size(118, 20);
			dateTimePickerETA.TabIndex = 188;
			dateTimePickerETA.TabStop = false;
			label13.AutoSize = true;
			label13.Location = new System.Drawing.Point(456, 7);
			label13.Name = "label13";
			label13.Size = new System.Drawing.Size(31, 13);
			label13.TabIndex = 187;
			label13.Text = "ETA:";
			textBoxPOSysDocID.BackColor = System.Drawing.Color.WhiteSmoke;
			textBoxPOSysDocID.Location = new System.Drawing.Point(93, 3);
			textBoxPOSysDocID.Name = "textBoxPOSysDocID";
			textBoxPOSysDocID.ReadOnly = true;
			textBoxPOSysDocID.Size = new System.Drawing.Size(32, 20);
			textBoxPOSysDocID.TabIndex = 182;
			textBoxPOSysDocID.TabStop = false;
			buttonSelectPO.AdjustImageLocation = new System.Drawing.Point(0, 0);
			buttonSelectPO.BackColor = System.Drawing.Color.DarkGray;
			buttonSelectPO.BtnShape = Micromind.UISupport.BtnShape.Rectangle;
			buttonSelectPO.BtnStyle = Micromind.UISupport.XPStyle.Default;
			buttonSelectPO.ImeMode = System.Windows.Forms.ImeMode.NoControl;
			buttonSelectPO.Location = new System.Drawing.Point(223, 1);
			buttonSelectPO.Name = "buttonSelectPO";
			buttonSelectPO.Size = new System.Drawing.Size(25, 24);
			buttonSelectPO.TabIndex = 180;
			buttonSelectPO.Text = "...";
			buttonSelectPO.UseVisualStyleBackColor = false;
			buttonSelectPO.Click += new System.EventHandler(buttonSelectPO_Click);
			textBoxPOVoucherID.BackColor = System.Drawing.Color.WhiteSmoke;
			textBoxPOVoucherID.Location = new System.Drawing.Point(127, 3);
			textBoxPOVoucherID.Name = "textBoxPOVoucherID";
			textBoxPOVoucherID.ReadOnly = true;
			textBoxPOVoucherID.Size = new System.Drawing.Size(95, 20);
			textBoxPOVoucherID.TabIndex = 181;
			textBoxPOVoucherID.TabStop = false;
			label9.AutoSize = true;
			label9.Location = new System.Drawing.Point(260, 6);
			label9.Name = "label9";
			label9.Size = new System.Drawing.Size(52, 13);
			label9.TabIndex = 170;
			label9.Text = "PO Term:";
			textBoxPOTerm.BackColor = System.Drawing.Color.WhiteSmoke;
			textBoxPOTerm.Location = new System.Drawing.Point(312, 3);
			textBoxPOTerm.Name = "textBoxPOTerm";
			textBoxPOTerm.ReadOnly = true;
			textBoxPOTerm.Size = new System.Drawing.Size(138, 20);
			textBoxPOTerm.TabIndex = 1;
			textBoxPOTerm.TabStop = false;
			label8.AutoSize = true;
			label8.Location = new System.Drawing.Point(371, 29);
			label8.Name = "label8";
			label8.Size = new System.Drawing.Size(49, 13);
			label8.TabIndex = 168;
			label8.Text = "Balance:";
			textBoxPOBalance.AllowDecimal = true;
			textBoxPOBalance.BackColor = System.Drawing.Color.WhiteSmoke;
			textBoxPOBalance.CustomReportFieldName = "";
			textBoxPOBalance.CustomReportKey = "";
			textBoxPOBalance.CustomReportValueType = 1;
			textBoxPOBalance.IsComboTextBox = false;
			textBoxPOBalance.IsModified = false;
			textBoxPOBalance.Location = new System.Drawing.Point(426, 26);
			textBoxPOBalance.MaxLength = 15;
			textBoxPOBalance.MaxValue = new decimal(new int[4]
			{
				-1,
				-1,
				-1,
				0
			});
			textBoxPOBalance.MinValue = new decimal(new int[4]
			{
				-1,
				-1,
				-1,
				-2147483648
			});
			textBoxPOBalance.Name = "textBoxPOBalance";
			textBoxPOBalance.NullText = "0";
			textBoxPOBalance.ReadOnly = true;
			textBoxPOBalance.Size = new System.Drawing.Size(93, 20);
			textBoxPOBalance.TabIndex = 4;
			textBoxPOBalance.Text = "0.00";
			textBoxPOBalance.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
			textBoxPOBalance.Value = new decimal(new int[4]
			{
				0,
				0,
				0,
				131072
			});
			label7.AutoSize = true;
			label7.Location = new System.Drawing.Point(232, 29);
			label7.Name = "label7";
			label7.Size = new System.Drawing.Size(31, 13);
			label7.TabIndex = 166;
			label7.Text = "Paid:";
			textBoxPOPaid.AllowDecimal = true;
			textBoxPOPaid.BackColor = System.Drawing.Color.WhiteSmoke;
			textBoxPOPaid.CustomReportFieldName = "";
			textBoxPOPaid.CustomReportKey = "";
			textBoxPOPaid.CustomReportValueType = 1;
			textBoxPOPaid.IsComboTextBox = false;
			textBoxPOPaid.IsModified = false;
			textBoxPOPaid.Location = new System.Drawing.Point(267, 26);
			textBoxPOPaid.MaxLength = 15;
			textBoxPOPaid.MaxValue = new decimal(new int[4]
			{
				-1,
				-1,
				-1,
				0
			});
			textBoxPOPaid.MinValue = new decimal(new int[4]
			{
				-1,
				-1,
				-1,
				-2147483648
			});
			textBoxPOPaid.Name = "textBoxPOPaid";
			textBoxPOPaid.NullText = "0";
			textBoxPOPaid.ReadOnly = true;
			textBoxPOPaid.Size = new System.Drawing.Size(93, 20);
			textBoxPOPaid.TabIndex = 3;
			textBoxPOPaid.Text = "0.00";
			textBoxPOPaid.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
			textBoxPOPaid.Value = new decimal(new int[4]
			{
				0,
				0,
				0,
				131072
			});
			label6.AutoSize = true;
			label6.Location = new System.Drawing.Point(9, 29);
			label6.Name = "label6";
			label6.Size = new System.Drawing.Size(64, 13);
			label6.TabIndex = 164;
			label6.Text = "PO Amount:";
			textBoxPOAmount.AllowDecimal = true;
			textBoxPOAmount.BackColor = System.Drawing.Color.WhiteSmoke;
			textBoxPOAmount.CustomReportFieldName = "";
			textBoxPOAmount.CustomReportKey = "";
			textBoxPOAmount.CustomReportValueType = 1;
			textBoxPOAmount.IsComboTextBox = false;
			textBoxPOAmount.IsModified = false;
			textBoxPOAmount.Location = new System.Drawing.Point(93, 26);
			textBoxPOAmount.MaxLength = 15;
			textBoxPOAmount.MaxValue = new decimal(new int[4]
			{
				-1,
				-1,
				-1,
				0
			});
			textBoxPOAmount.MinValue = new decimal(new int[4]
			{
				-1,
				-1,
				-1,
				-2147483648
			});
			textBoxPOAmount.Name = "textBoxPOAmount";
			textBoxPOAmount.NullText = "0";
			textBoxPOAmount.ReadOnly = true;
			textBoxPOAmount.Size = new System.Drawing.Size(129, 20);
			textBoxPOAmount.TabIndex = 2;
			textBoxPOAmount.Text = "0.00";
			textBoxPOAmount.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
			textBoxPOAmount.Value = new decimal(new int[4]
			{
				0,
				0,
				0,
				131072
			});
			label5.AutoSize = true;
			label5.Location = new System.Drawing.Point(9, 6);
			label5.Name = "label5";
			label5.Size = new System.Drawing.Size(84, 13);
			label5.TabIndex = 162;
			label5.Text = "Purchase Order:";
			paymentTermComboBox1.Assigned = false;
			paymentTermComboBox1.AutoCompleteMode = Infragistics.Win.AutoCompleteMode.Append;
			paymentTermComboBox1.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper;
			paymentTermComboBox1.CustomReportFieldName = "";
			paymentTermComboBox1.CustomReportKey = "";
			paymentTermComboBox1.CustomReportValueType = 1;
			paymentTermComboBox1.DescriptionTextBox = textBoxPOTerm;
			appearance65.BackColor = System.Drawing.SystemColors.Window;
			appearance65.BorderColor = System.Drawing.SystemColors.InactiveCaption;
			paymentTermComboBox1.DisplayLayout.Appearance = appearance65;
			paymentTermComboBox1.DisplayLayout.BorderStyle = Infragistics.Win.UIElementBorderStyle.Solid;
			paymentTermComboBox1.DisplayLayout.CaptionVisible = Infragistics.Win.DefaultableBoolean.False;
			appearance66.BackColor = System.Drawing.SystemColors.ActiveBorder;
			appearance66.BackColor2 = System.Drawing.SystemColors.ControlDark;
			appearance66.BackGradientStyle = Infragistics.Win.GradientStyle.Vertical;
			appearance66.BorderColor = System.Drawing.SystemColors.Window;
			paymentTermComboBox1.DisplayLayout.GroupByBox.Appearance = appearance66;
			appearance67.ForeColor = System.Drawing.SystemColors.GrayText;
			paymentTermComboBox1.DisplayLayout.GroupByBox.BandLabelAppearance = appearance67;
			paymentTermComboBox1.DisplayLayout.GroupByBox.BorderStyle = Infragistics.Win.UIElementBorderStyle.Solid;
			appearance68.BackColor = System.Drawing.SystemColors.ControlLightLight;
			appearance68.BackColor2 = System.Drawing.SystemColors.Control;
			appearance68.BackGradientStyle = Infragistics.Win.GradientStyle.Horizontal;
			appearance68.ForeColor = System.Drawing.SystemColors.GrayText;
			paymentTermComboBox1.DisplayLayout.GroupByBox.PromptAppearance = appearance68;
			paymentTermComboBox1.DisplayLayout.MaxColScrollRegions = 1;
			paymentTermComboBox1.DisplayLayout.MaxRowScrollRegions = 1;
			appearance69.BackColor = System.Drawing.SystemColors.Window;
			appearance69.ForeColor = System.Drawing.SystemColors.ControlText;
			paymentTermComboBox1.DisplayLayout.Override.ActiveCellAppearance = appearance69;
			appearance70.BackColor = System.Drawing.SystemColors.Highlight;
			appearance70.ForeColor = System.Drawing.SystemColors.HighlightText;
			paymentTermComboBox1.DisplayLayout.Override.ActiveRowAppearance = appearance70;
			paymentTermComboBox1.DisplayLayout.Override.BorderStyleCell = Infragistics.Win.UIElementBorderStyle.Dotted;
			paymentTermComboBox1.DisplayLayout.Override.BorderStyleRow = Infragistics.Win.UIElementBorderStyle.Dotted;
			appearance71.BackColor = System.Drawing.SystemColors.Window;
			paymentTermComboBox1.DisplayLayout.Override.CardAreaAppearance = appearance71;
			appearance72.BorderColor = System.Drawing.Color.Silver;
			appearance72.TextTrimming = Infragistics.Win.TextTrimming.EllipsisCharacter;
			paymentTermComboBox1.DisplayLayout.Override.CellAppearance = appearance72;
			paymentTermComboBox1.DisplayLayout.Override.CellClickAction = Infragistics.Win.UltraWinGrid.CellClickAction.EditAndSelectText;
			paymentTermComboBox1.DisplayLayout.Override.CellPadding = 0;
			appearance73.BackColor = System.Drawing.SystemColors.Control;
			appearance73.BackColor2 = System.Drawing.SystemColors.ControlDark;
			appearance73.BackGradientAlignment = Infragistics.Win.GradientAlignment.Element;
			appearance73.BackGradientStyle = Infragistics.Win.GradientStyle.Horizontal;
			appearance73.BorderColor = System.Drawing.SystemColors.Window;
			paymentTermComboBox1.DisplayLayout.Override.GroupByRowAppearance = appearance73;
			appearance74.TextHAlignAsString = "Left";
			paymentTermComboBox1.DisplayLayout.Override.HeaderAppearance = appearance74;
			paymentTermComboBox1.DisplayLayout.Override.HeaderClickAction = Infragistics.Win.UltraWinGrid.HeaderClickAction.SortMulti;
			paymentTermComboBox1.DisplayLayout.Override.HeaderStyle = Infragistics.Win.HeaderStyle.WindowsXPCommand;
			appearance75.BackColor = System.Drawing.SystemColors.Window;
			appearance75.BorderColor = System.Drawing.Color.Silver;
			paymentTermComboBox1.DisplayLayout.Override.RowAppearance = appearance75;
			paymentTermComboBox1.DisplayLayout.Override.RowSelectors = Infragistics.Win.DefaultableBoolean.False;
			appearance76.BackColor = System.Drawing.SystemColors.ControlLight;
			paymentTermComboBox1.DisplayLayout.Override.TemplateAddRowAppearance = appearance76;
			paymentTermComboBox1.DisplayLayout.ScrollBounds = Infragistics.Win.UltraWinGrid.ScrollBounds.ScrollToFill;
			paymentTermComboBox1.DisplayLayout.ScrollStyle = Infragistics.Win.UltraWinGrid.ScrollStyle.Immediate;
			paymentTermComboBox1.DisplayLayout.ViewStyleBand = Infragistics.Win.UltraWinGrid.ViewStyleBand.OutlookGroupBy;
			paymentTermComboBox1.DropDownSearchMethod = Infragistics.Win.UltraWinGrid.DropDownSearchMethod.Linear;
			paymentTermComboBox1.Editable = true;
			paymentTermComboBox1.FilterString = "";
			paymentTermComboBox1.HasAllAccount = false;
			paymentTermComboBox1.HasCustom = false;
			paymentTermComboBox1.IsDataLoaded = false;
			paymentTermComboBox1.Location = new System.Drawing.Point(339, 3);
			paymentTermComboBox1.MaxDropDownItems = 12;
			paymentTermComboBox1.Name = "paymentTermComboBox1";
			paymentTermComboBox1.ShowInactiveItems = false;
			paymentTermComboBox1.ShowQuickAdd = true;
			paymentTermComboBox1.Size = new System.Drawing.Size(100, 20);
			paymentTermComboBox1.TabIndex = 180;
			paymentTermComboBox1.UseFlatMode = Infragistics.Win.DefaultableBoolean.True;
			paymentTermComboBox1.Visible = false;
			comboBoxPOTerm.Assigned = false;
			comboBoxPOTerm.AutoCompleteMode = Infragistics.Win.AutoCompleteMode.Append;
			comboBoxPOTerm.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper;
			comboBoxPOTerm.CustomReportFieldName = "";
			comboBoxPOTerm.CustomReportKey = "";
			comboBoxPOTerm.CustomReportValueType = 1;
			comboBoxPOTerm.DescriptionTextBox = null;
			appearance77.BackColor = System.Drawing.SystemColors.Window;
			appearance77.BorderColor = System.Drawing.SystemColors.InactiveCaption;
			comboBoxPOTerm.DisplayLayout.Appearance = appearance77;
			comboBoxPOTerm.DisplayLayout.BorderStyle = Infragistics.Win.UIElementBorderStyle.Solid;
			comboBoxPOTerm.DisplayLayout.CaptionVisible = Infragistics.Win.DefaultableBoolean.False;
			appearance78.BackColor = System.Drawing.SystemColors.ActiveBorder;
			appearance78.BackColor2 = System.Drawing.SystemColors.ControlDark;
			appearance78.BackGradientStyle = Infragistics.Win.GradientStyle.Vertical;
			appearance78.BorderColor = System.Drawing.SystemColors.Window;
			comboBoxPOTerm.DisplayLayout.GroupByBox.Appearance = appearance78;
			appearance79.ForeColor = System.Drawing.SystemColors.GrayText;
			comboBoxPOTerm.DisplayLayout.GroupByBox.BandLabelAppearance = appearance79;
			comboBoxPOTerm.DisplayLayout.GroupByBox.BorderStyle = Infragistics.Win.UIElementBorderStyle.Solid;
			appearance80.BackColor = System.Drawing.SystemColors.ControlLightLight;
			appearance80.BackColor2 = System.Drawing.SystemColors.Control;
			appearance80.BackGradientStyle = Infragistics.Win.GradientStyle.Horizontal;
			appearance80.ForeColor = System.Drawing.SystemColors.GrayText;
			comboBoxPOTerm.DisplayLayout.GroupByBox.PromptAppearance = appearance80;
			comboBoxPOTerm.DisplayLayout.MaxColScrollRegions = 1;
			comboBoxPOTerm.DisplayLayout.MaxRowScrollRegions = 1;
			appearance81.BackColor = System.Drawing.SystemColors.Window;
			appearance81.ForeColor = System.Drawing.SystemColors.ControlText;
			comboBoxPOTerm.DisplayLayout.Override.ActiveCellAppearance = appearance81;
			appearance82.BackColor = System.Drawing.SystemColors.Highlight;
			appearance82.ForeColor = System.Drawing.SystemColors.HighlightText;
			comboBoxPOTerm.DisplayLayout.Override.ActiveRowAppearance = appearance82;
			comboBoxPOTerm.DisplayLayout.Override.BorderStyleCell = Infragistics.Win.UIElementBorderStyle.Dotted;
			comboBoxPOTerm.DisplayLayout.Override.BorderStyleRow = Infragistics.Win.UIElementBorderStyle.Dotted;
			appearance83.BackColor = System.Drawing.SystemColors.Window;
			comboBoxPOTerm.DisplayLayout.Override.CardAreaAppearance = appearance83;
			appearance84.BorderColor = System.Drawing.Color.Silver;
			appearance84.TextTrimming = Infragistics.Win.TextTrimming.EllipsisCharacter;
			comboBoxPOTerm.DisplayLayout.Override.CellAppearance = appearance84;
			comboBoxPOTerm.DisplayLayout.Override.CellClickAction = Infragistics.Win.UltraWinGrid.CellClickAction.EditAndSelectText;
			comboBoxPOTerm.DisplayLayout.Override.CellPadding = 0;
			appearance85.BackColor = System.Drawing.SystemColors.Control;
			appearance85.BackColor2 = System.Drawing.SystemColors.ControlDark;
			appearance85.BackGradientAlignment = Infragistics.Win.GradientAlignment.Element;
			appearance85.BackGradientStyle = Infragistics.Win.GradientStyle.Horizontal;
			appearance85.BorderColor = System.Drawing.SystemColors.Window;
			comboBoxPOTerm.DisplayLayout.Override.GroupByRowAppearance = appearance85;
			appearance86.TextHAlignAsString = "Left";
			comboBoxPOTerm.DisplayLayout.Override.HeaderAppearance = appearance86;
			comboBoxPOTerm.DisplayLayout.Override.HeaderClickAction = Infragistics.Win.UltraWinGrid.HeaderClickAction.SortMulti;
			comboBoxPOTerm.DisplayLayout.Override.HeaderStyle = Infragistics.Win.HeaderStyle.WindowsXPCommand;
			appearance87.BackColor = System.Drawing.SystemColors.Window;
			appearance87.BorderColor = System.Drawing.Color.Silver;
			comboBoxPOTerm.DisplayLayout.Override.RowAppearance = appearance87;
			comboBoxPOTerm.DisplayLayout.Override.RowSelectors = Infragistics.Win.DefaultableBoolean.False;
			appearance88.BackColor = System.Drawing.SystemColors.ControlLight;
			comboBoxPOTerm.DisplayLayout.Override.TemplateAddRowAppearance = appearance88;
			comboBoxPOTerm.DisplayLayout.ScrollBounds = Infragistics.Win.UltraWinGrid.ScrollBounds.ScrollToFill;
			comboBoxPOTerm.DisplayLayout.ScrollStyle = Infragistics.Win.UltraWinGrid.ScrollStyle.Immediate;
			comboBoxPOTerm.DisplayLayout.ViewStyleBand = Infragistics.Win.UltraWinGrid.ViewStyleBand.OutlookGroupBy;
			comboBoxPOTerm.DropDownSearchMethod = Infragistics.Win.UltraWinGrid.DropDownSearchMethod.Linear;
			comboBoxPOTerm.Editable = true;
			comboBoxPOTerm.FilterString = "";
			comboBoxPOTerm.HasAllAccount = false;
			comboBoxPOTerm.HasCustom = false;
			comboBoxPOTerm.IsDataLoaded = false;
			comboBoxPOTerm.Location = new System.Drawing.Point(341, 4);
			comboBoxPOTerm.MaxDropDownItems = 12;
			comboBoxPOTerm.Name = "comboBoxPOTerm";
			comboBoxPOTerm.ShowInactiveItems = false;
			comboBoxPOTerm.ShowQuickAdd = true;
			comboBoxPOTerm.Size = new System.Drawing.Size(100, 20);
			comboBoxPOTerm.TabIndex = 180;
			comboBoxPOTerm.UseFlatMode = Infragistics.Win.DefaultableBoolean.True;
			comboBoxPOTerm.Visible = false;
			toolStripButtonFirst.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
			toolStripButtonFirst.Image = Micromind.ClientUI.Properties.Resources.first;
			toolStripButtonFirst.ImageTransparentColor = System.Drawing.Color.Magenta;
			toolStripButtonFirst.Name = "toolStripButtonFirst";
			toolStripButtonFirst.Size = new System.Drawing.Size(28, 28);
			toolStripButtonFirst.Text = "First Record";
			toolStripButtonFirst.Click += new System.EventHandler(toolStripButtonFirst_Click);
			toolStripButtonPrevious.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
			toolStripButtonPrevious.Image = Micromind.ClientUI.Properties.Resources.prev;
			toolStripButtonPrevious.ImageTransparentColor = System.Drawing.Color.Magenta;
			toolStripButtonPrevious.Name = "toolStripButtonPrevious";
			toolStripButtonPrevious.Size = new System.Drawing.Size(28, 28);
			toolStripButtonPrevious.Text = "Previous Record";
			toolStripButtonPrevious.Click += new System.EventHandler(toolStripButtonPrevious_Click);
			toolStripButtonNext.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
			toolStripButtonNext.Image = Micromind.ClientUI.Properties.Resources.next;
			toolStripButtonNext.ImageTransparentColor = System.Drawing.Color.Magenta;
			toolStripButtonNext.Name = "toolStripButtonNext";
			toolStripButtonNext.Size = new System.Drawing.Size(28, 28);
			toolStripButtonNext.Text = "Next Record";
			toolStripButtonNext.Click += new System.EventHandler(toolStripButtonNext_Click);
			toolStripButtonLast.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
			toolStripButtonLast.Image = Micromind.ClientUI.Properties.Resources.last;
			toolStripButtonLast.ImageTransparentColor = System.Drawing.Color.Magenta;
			toolStripButtonLast.Name = "toolStripButtonLast";
			toolStripButtonLast.Size = new System.Drawing.Size(28, 28);
			toolStripButtonLast.Text = "Last Record";
			toolStripButtonLast.Click += new System.EventHandler(toolStripButtonLast_Click);
			toolStripSeparator1.Name = "toolStripSeparator1";
			toolStripSeparator1.Size = new System.Drawing.Size(6, 31);
			toolStripButtonOpenList.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
			toolStripButtonOpenList.Image = Micromind.ClientUI.Properties.Resources.list;
			toolStripButtonOpenList.ImageTransparentColor = System.Drawing.Color.Magenta;
			toolStripButtonOpenList.Name = "toolStripButtonOpenList";
			toolStripButtonOpenList.Size = new System.Drawing.Size(28, 28);
			toolStripButtonOpenList.Text = "Open List";
			toolStripButtonOpenList.Click += new System.EventHandler(toolStripButtonOpenList_Click);
			toolStripSeparator5.Name = "toolStripSeparator5";
			toolStripSeparator5.Size = new System.Drawing.Size(6, 31);
			toolStripTextBoxFind.Name = "toolStripTextBoxFind";
			toolStripTextBoxFind.Size = new System.Drawing.Size(100, 31);
			toolStripTextBoxFind.KeyPress += new System.Windows.Forms.KeyPressEventHandler(toolStripTextBoxFind_KeyPress);
			toolStripButtonFind.Image = Micromind.ClientUI.Properties.Resources.find;
			toolStripButtonFind.ImageTransparentColor = System.Drawing.Color.Magenta;
			toolStripButtonFind.Name = "toolStripButtonFind";
			toolStripButtonFind.Size = new System.Drawing.Size(58, 28);
			toolStripButtonFind.Text = "Find";
			toolStripButtonFind.Click += new System.EventHandler(toolStripButtonFind_Click);
			toolStripSeparator2.Name = "toolStripSeparator2";
			toolStripSeparator2.Size = new System.Drawing.Size(6, 31);
			toolStripButtonPreview.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
			toolStripButtonPreview.Image = Micromind.ClientUI.Properties.Resources.preview;
			toolStripButtonPreview.ImageTransparentColor = System.Drawing.Color.Magenta;
			toolStripButtonPreview.Name = "toolStripButtonPreview";
			toolStripButtonPreview.Size = new System.Drawing.Size(28, 28);
			toolStripButtonPreview.Text = "Preview";
			toolStripButtonPreview.ToolTipText = "Preview";
			toolStripButtonPreview.Click += new System.EventHandler(toolStripButtonPreview_Click);
			toolStripButtonPrint.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
			toolStripButtonPrint.Image = Micromind.ClientUI.Properties.Resources.printer;
			toolStripButtonPrint.ImageTransparentColor = System.Drawing.Color.Magenta;
			toolStripButtonPrint.Name = "toolStripButtonPrint";
			toolStripButtonPrint.Size = new System.Drawing.Size(28, 28);
			toolStripButtonPrint.Text = "&Print";
			toolStripButtonPrint.ToolTipText = "Print (Ctrl+P)";
			toolStripButtonPrint.Click += new System.EventHandler(toolStripButtonPrint_Click);
			toolStripSeparator7.Name = "toolStripSeparator7";
			toolStripSeparator7.Size = new System.Drawing.Size(6, 31);
			toolStripButtonAttach.Image = Micromind.ClientUI.Properties.Resources.attach_24x24;
			toolStripButtonAttach.ImageTransparentColor = System.Drawing.Color.Magenta;
			toolStripButtonAttach.Name = "toolStripButtonAttach";
			toolStripButtonAttach.Size = new System.Drawing.Size(91, 28);
			toolStripButtonAttach.Text = "Attach File";
			toolStripButtonAttach.Click += new System.EventHandler(toolStripButtonAttach_Click);
			toolStripSeparator4.Name = "toolStripSeparator4";
			toolStripSeparator4.Size = new System.Drawing.Size(6, 31);
			toolStripDropDownButton1.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Text;
			toolStripDropDownButton1.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[4]
			{
				duplicateToolStripMenuItem,
				toolStripSeparator6,
				saveDraftToolStripMenuItem,
				loadDraftToolStripMenuItem
			});
			toolStripDropDownButton1.Image = (System.Drawing.Image)resources.GetObject("toolStripDropDownButton1.Image");
			toolStripDropDownButton1.ImageTransparentColor = System.Drawing.Color.Magenta;
			toolStripDropDownButton1.Name = "toolStripDropDownButton1";
			toolStripDropDownButton1.Size = new System.Drawing.Size(60, 28);
			toolStripDropDownButton1.Text = "Actions";
			toolStripDropDownButton1.DropDownOpening += new System.EventHandler(toolStripDropDownButton1_DropDownOpening);
			duplicateToolStripMenuItem.Name = "duplicateToolStripMenuItem";
			duplicateToolStripMenuItem.Size = new System.Drawing.Size(141, 22);
			duplicateToolStripMenuItem.Text = "Duplicate";
			duplicateToolStripMenuItem.Click += new System.EventHandler(duplicateToolStripMenuItem_Click);
			toolStripSeparator6.Name = "toolStripSeparator6";
			toolStripSeparator6.Size = new System.Drawing.Size(138, 6);
			saveDraftToolStripMenuItem.Name = "saveDraftToolStripMenuItem";
			saveDraftToolStripMenuItem.Size = new System.Drawing.Size(141, 22);
			saveDraftToolStripMenuItem.Text = "Save as Draft";
			saveDraftToolStripMenuItem.Click += new System.EventHandler(saveDraftToolStripMenuItem_Click);
			loadDraftToolStripMenuItem.Name = "loadDraftToolStripMenuItem";
			loadDraftToolStripMenuItem.Size = new System.Drawing.Size(141, 22);
			loadDraftToolStripMenuItem.Text = "Load Draft...";
			loadDraftToolStripMenuItem.Click += new System.EventHandler(loadDraftToolStripMenuItem_Click);
			toolStripButtonApproval.Alignment = System.Windows.Forms.ToolStripItemAlignment.Right;
			toolStripButtonApproval.AutoSize = false;
			toolStripButtonApproval.BackColor = System.Drawing.Color.Transparent;
			toolStripButtonApproval.Font = new System.Drawing.Font("Segoe UI", 9f, System.Drawing.FontStyle.Bold);
			toolStripButtonApproval.ForeColor = System.Drawing.Color.Green;
			toolStripButtonApproval.ImageScaling = System.Windows.Forms.ToolStripItemImageScaling.None;
			toolStripButtonApproval.ImageTransparentColor = System.Drawing.Color.Magenta;
			toolStripButtonApproval.Name = "toolStripButtonApproval";
			toolStripButtonApproval.Overflow = System.Windows.Forms.ToolStripItemOverflow.Never;
			toolStripButtonApproval.Size = new System.Drawing.Size(70, 22);
			toolStripButtonApproval.Text = "Pending";
			toolStripLabelApproval.Alignment = System.Windows.Forms.ToolStripItemAlignment.Right;
			toolStripLabelApproval.Font = new System.Drawing.Font("Segoe UI", 9f, System.Drawing.FontStyle.Bold);
			toolStripLabelApproval.Name = "toolStripLabelApproval";
			toolStripLabelApproval.Size = new System.Drawing.Size(45, 15);
			toolStripLabelApproval.Text = "Status:";
			toolStripSeparatorApproval.Alignment = System.Windows.Forms.ToolStripItemAlignment.Right;
			toolStripSeparatorApproval.Name = "toolStripSeparatorApproval";
			toolStripSeparatorApproval.Size = new System.Drawing.Size(6, 31);
			toolStripButtonPrintTemplate.Image = (System.Drawing.Image)resources.GetObject("toolStripButtonPrintTemplate.Image");
			toolStripButtonPrintTemplate.ImageTransparentColor = System.Drawing.Color.Magenta;
			toolStripButtonPrintTemplate.Name = "toolStripButtonPrintTemplate";
			toolStripButtonPrintTemplate.Size = new System.Drawing.Size(77, 28);
			toolStripButtonPrintTemplate.Text = "Print TR";
			toolStripButtonPrintTemplate.Visible = false;
			toolStripButtonPrintTemplate.Click += new System.EventHandler(toolStripButtonPrintTemplate_Click);
			toolStripButtonInformation.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
			toolStripButtonInformation.Image = Micromind.ClientUI.Properties.Resources.docinfo_24x24;
			toolStripButtonInformation.ImageTransparentColor = System.Drawing.Color.Magenta;
			toolStripButtonInformation.Name = "toolStripButtonInformation";
			toolStripButtonInformation.Size = new System.Drawing.Size(28, 28);
			toolStripButtonInformation.Text = "Document Information";
			toolStripButtonInformation.Click += new System.EventHandler(toolStripButtonInformation_Click_1);
			toolStrip1.GripStyle = System.Windows.Forms.ToolStripGripStyle.Hidden;
			toolStrip1.ImageScalingSize = new System.Drawing.Size(24, 24);
			toolStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[22]
			{
				toolStripButtonFirst,
				toolStripButtonPrevious,
				toolStripButtonNext,
				toolStripButtonLast,
				toolStripSeparator1,
				toolStripButtonOpenList,
				toolStripSeparator5,
				toolStripTextBoxFind,
				toolStripButtonFind,
				toolStripSeparator2,
				toolStripButtonPreview,
				toolStripButtonPrint,
				toolStripButtonMultiPreview,
				toolStripSeparator7,
				toolStripButtonAttach,
				toolStripSeparator4,
				toolStripDropDownButton1,
				toolStripButtonApproval,
				toolStripLabelApproval,
				toolStripSeparatorApproval,
				toolStripButtonPrintTemplate,
				toolStripButtonInformation
			});
			toolStrip1.Location = new System.Drawing.Point(0, 0);
			toolStrip1.Name = "toolStrip1";
			toolStrip1.Size = new System.Drawing.Size(664, 31);
			toolStrip1.TabIndex = 0;
			toolStrip1.Text = "toolStrip1";
			toolStripButtonMultiPreview.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
			toolStripButtonMultiPreview.Image = Micromind.ClientUI.Properties.Resources.multi_doc;
			toolStripButtonMultiPreview.ImageTransparentColor = System.Drawing.Color.Magenta;
			toolStripButtonMultiPreview.Name = "toolStripButtonMultiPreview";
			toolStripButtonMultiPreview.Size = new System.Drawing.Size(28, 28);
			toolStripButtonMultiPreview.Text = "MultiPreview";
			toolStripButtonMultiPreview.Click += new System.EventHandler(toolStripButtonMultiPreview_Click);
			buttonSelectInvoice.AdjustImageLocation = new System.Drawing.Point(0, 0);
			buttonSelectInvoice.BackColor = System.Drawing.Color.DarkGray;
			buttonSelectInvoice.BtnShape = Micromind.UISupport.BtnShape.Rectangle;
			buttonSelectInvoice.BtnStyle = Micromind.UISupport.XPStyle.Default;
			buttonSelectInvoice.ImeMode = System.Windows.Forms.ImeMode.NoControl;
			buttonSelectInvoice.Location = new System.Drawing.Point(213, 253);
			buttonSelectInvoice.Name = "buttonSelectInvoice";
			buttonSelectInvoice.Size = new System.Drawing.Size(27, 21);
			buttonSelectInvoice.TabIndex = 7;
			buttonSelectInvoice.Text = "...";
			buttonSelectInvoice.UseVisualStyleBackColor = false;
			buttonSelectInvoice.Click += new System.EventHandler(buttonSelectInvoice_Click);
			formManager.BackColor = System.Drawing.Color.RosyBrown;
			formManager.Dock = System.Windows.Forms.DockStyle.Left;
			formManager.IsForcedDirty = false;
			formManager.Location = new System.Drawing.Point(0, 31);
			formManager.MaximumSize = new System.Drawing.Size(20, 20);
			formManager.MinimumSize = new System.Drawing.Size(20, 20);
			formManager.Name = "formManager";
			formManager.Size = new System.Drawing.Size(20, 20);
			formManager.TabIndex = 16;
			formManager.Text = "formManager1";
			formManager.Visible = false;
			datePickerDueDate.Format = System.Windows.Forms.DateTimePickerFormat.Short;
			datePickerDueDate.Location = new System.Drawing.Point(464, 229);
			datePickerDueDate.Name = "datePickerDueDate";
			datePickerDueDate.Size = new System.Drawing.Size(127, 20);
			datePickerDueDate.TabIndex = 7;
			datePickerDueDate.Value = new System.DateTime(2015, 5, 13, 0, 0, 0, 0);
			textBoxAmount.AllowDecimal = true;
			textBoxAmount.CustomReportFieldName = "";
			textBoxAmount.CustomReportKey = "";
			textBoxAmount.CustomReportValueType = 1;
			textBoxAmount.IsComboTextBox = false;
			textBoxAmount.IsModified = false;
			textBoxAmount.Location = new System.Drawing.Point(100, 253);
			textBoxAmount.MaxLength = 15;
			textBoxAmount.MaxValue = new decimal(new int[4]
			{
				-1,
				-1,
				-1,
				0
			});
			textBoxAmount.MinValue = new decimal(new int[4]
			{
				-1,
				-1,
				-1,
				-2147483648
			});
			textBoxAmount.Name = "textBoxAmount";
			textBoxAmount.NullText = "0";
			textBoxAmount.Size = new System.Drawing.Size(111, 20);
			textBoxAmount.TabIndex = 5;
			textBoxAmount.Text = "0.00";
			textBoxAmount.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
			textBoxAmount.Value = new decimal(new int[4]
			{
				0,
				0,
				0,
				131072
			});
			textBoxAmount.TextChanged += new System.EventHandler(textBoxAmount_TextChanged);
			mmLabel7.AutoSize = true;
			mmLabel7.BackColor = System.Drawing.Color.Transparent;
			mmLabel7.BorderColor = System.Drawing.Color.FromArgb(78, 122, 171);
			mmLabel7.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25f, System.Drawing.FontStyle.Bold);
			mmLabel7.IsFieldHeader = false;
			mmLabel7.IsRequired = true;
			mmLabel7.Location = new System.Drawing.Point(393, 232);
			mmLabel7.Name = "mmLabel7";
			mmLabel7.PenWidth = 1f;
			mmLabel7.ShowBorder = false;
			mmLabel7.Size = new System.Drawing.Size(65, 13);
			mmLabel7.TabIndex = 2;
			mmLabel7.Text = "Due Date:";
			comboBoxFacility.Assigned = false;
			comboBoxFacility.AutoCompleteMode = Infragistics.Win.AutoCompleteMode.Append;
			comboBoxFacility.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper;
			comboBoxFacility.CustomReportFieldName = "";
			comboBoxFacility.CustomReportKey = "";
			comboBoxFacility.CustomReportValueType = 1;
			comboBoxFacility.DescriptionTextBox = textBoxFacilityName;
			appearance89.BackColor = System.Drawing.SystemColors.Window;
			appearance89.BorderColor = System.Drawing.SystemColors.InactiveCaption;
			comboBoxFacility.DisplayLayout.Appearance = appearance89;
			comboBoxFacility.DisplayLayout.BorderStyle = Infragistics.Win.UIElementBorderStyle.Solid;
			comboBoxFacility.DisplayLayout.CaptionVisible = Infragistics.Win.DefaultableBoolean.False;
			appearance90.BackColor = System.Drawing.SystemColors.ActiveBorder;
			appearance90.BackColor2 = System.Drawing.SystemColors.ControlDark;
			appearance90.BackGradientStyle = Infragistics.Win.GradientStyle.Vertical;
			appearance90.BorderColor = System.Drawing.SystemColors.Window;
			comboBoxFacility.DisplayLayout.GroupByBox.Appearance = appearance90;
			appearance91.ForeColor = System.Drawing.SystemColors.GrayText;
			comboBoxFacility.DisplayLayout.GroupByBox.BandLabelAppearance = appearance91;
			comboBoxFacility.DisplayLayout.GroupByBox.BorderStyle = Infragistics.Win.UIElementBorderStyle.Solid;
			appearance92.BackColor = System.Drawing.SystemColors.ControlLightLight;
			appearance92.BackColor2 = System.Drawing.SystemColors.Control;
			appearance92.BackGradientStyle = Infragistics.Win.GradientStyle.Horizontal;
			appearance92.ForeColor = System.Drawing.SystemColors.GrayText;
			comboBoxFacility.DisplayLayout.GroupByBox.PromptAppearance = appearance92;
			comboBoxFacility.DisplayLayout.MaxColScrollRegions = 1;
			comboBoxFacility.DisplayLayout.MaxRowScrollRegions = 1;
			appearance93.BackColor = System.Drawing.SystemColors.Window;
			appearance93.ForeColor = System.Drawing.SystemColors.ControlText;
			comboBoxFacility.DisplayLayout.Override.ActiveCellAppearance = appearance93;
			appearance94.BackColor = System.Drawing.SystemColors.Highlight;
			appearance94.ForeColor = System.Drawing.SystemColors.HighlightText;
			comboBoxFacility.DisplayLayout.Override.ActiveRowAppearance = appearance94;
			comboBoxFacility.DisplayLayout.Override.BorderStyleCell = Infragistics.Win.UIElementBorderStyle.Dotted;
			comboBoxFacility.DisplayLayout.Override.BorderStyleRow = Infragistics.Win.UIElementBorderStyle.Dotted;
			appearance95.BackColor = System.Drawing.SystemColors.Window;
			comboBoxFacility.DisplayLayout.Override.CardAreaAppearance = appearance95;
			appearance96.BorderColor = System.Drawing.Color.Silver;
			appearance96.TextTrimming = Infragistics.Win.TextTrimming.EllipsisCharacter;
			comboBoxFacility.DisplayLayout.Override.CellAppearance = appearance96;
			comboBoxFacility.DisplayLayout.Override.CellClickAction = Infragistics.Win.UltraWinGrid.CellClickAction.EditAndSelectText;
			comboBoxFacility.DisplayLayout.Override.CellPadding = 0;
			appearance97.BackColor = System.Drawing.SystemColors.Control;
			appearance97.BackColor2 = System.Drawing.SystemColors.ControlDark;
			appearance97.BackGradientAlignment = Infragistics.Win.GradientAlignment.Element;
			appearance97.BackGradientStyle = Infragistics.Win.GradientStyle.Horizontal;
			appearance97.BorderColor = System.Drawing.SystemColors.Window;
			comboBoxFacility.DisplayLayout.Override.GroupByRowAppearance = appearance97;
			appearance98.TextHAlignAsString = "Left";
			comboBoxFacility.DisplayLayout.Override.HeaderAppearance = appearance98;
			comboBoxFacility.DisplayLayout.Override.HeaderClickAction = Infragistics.Win.UltraWinGrid.HeaderClickAction.SortMulti;
			comboBoxFacility.DisplayLayout.Override.HeaderStyle = Infragistics.Win.HeaderStyle.WindowsXPCommand;
			appearance99.BackColor = System.Drawing.SystemColors.Window;
			appearance99.BorderColor = System.Drawing.Color.Silver;
			comboBoxFacility.DisplayLayout.Override.RowAppearance = appearance99;
			comboBoxFacility.DisplayLayout.Override.RowSelectors = Infragistics.Win.DefaultableBoolean.False;
			appearance100.BackColor = System.Drawing.SystemColors.ControlLight;
			comboBoxFacility.DisplayLayout.Override.TemplateAddRowAppearance = appearance100;
			comboBoxFacility.DisplayLayout.ScrollBounds = Infragistics.Win.UltraWinGrid.ScrollBounds.ScrollToFill;
			comboBoxFacility.DisplayLayout.ScrollStyle = Infragistics.Win.UltraWinGrid.ScrollStyle.Immediate;
			comboBoxFacility.DisplayLayout.ViewStyleBand = Infragistics.Win.UltraWinGrid.ViewStyleBand.OutlookGroupBy;
			comboBoxFacility.DropDownSearchMethod = Infragistics.Win.UltraWinGrid.DropDownSearchMethod.Linear;
			comboBoxFacility.Editable = true;
			comboBoxFacility.FilterFacilityType = Micromind.Common.Data.BankFacilityTypes.TR;
			comboBoxFacility.FilterString = "";
			comboBoxFacility.HasAllAccount = false;
			comboBoxFacility.HasCustom = false;
			comboBoxFacility.IsDataLoaded = false;
			comboBoxFacility.Location = new System.Drawing.Point(100, 206);
			comboBoxFacility.MaxDropDownItems = 12;
			comboBoxFacility.Name = "comboBoxFacility";
			comboBoxFacility.ShowInactiveItems = false;
			comboBoxFacility.ShowQuickAdd = true;
			comboBoxFacility.Size = new System.Drawing.Size(111, 20);
			comboBoxFacility.TabIndex = 1;
			comboBoxFacility.UseFlatMode = Infragistics.Win.DefaultableBoolean.True;
			comboBoxFacility.SelectedIndexChanged += new System.EventHandler(comboBoxFacility_SelectedIndexChanged);
			base.AutoScaleDimensions = new System.Drawing.SizeF(6f, 13f);
			base.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			BackColor = System.Drawing.Color.WhiteSmoke;
			base.ClientSize = new System.Drawing.Size(664, 387);
			base.Controls.Add(ultraFormattedLinkLabel8);
			base.Controls.Add(buttonSelectInvoice);
			base.Controls.Add(ultraFormattedLinkLabel4);
			base.Controls.Add(numericUpDownTenorDay);
			base.Controls.Add(panelDetails);
			base.Controls.Add(textBoxRegBalance);
			base.Controls.Add(formManager);
			base.Controls.Add(label19);
			base.Controls.Add(panelButtons);
			base.Controls.Add(datePickerDueDate);
			base.Controls.Add(toolStrip1);
			base.Controls.Add(textBoxRef1);
			base.Controls.Add(labelAmountBase);
			base.Controls.Add(textBoxFacilityName);
			base.Controls.Add(textBoxAmount);
			base.Controls.Add(mmLabel7);
			base.Controls.Add(label21);
			base.Controls.Add(comboBoxFacility);
			base.Controls.Add(textBoxAmountBase);
			base.Controls.Add(label22);
			base.Controls.Add(panel1);
			base.Icon = (System.Drawing.Icon)resources.GetObject("$this.Icon");
			base.KeyPreview = true;
			MinimumSize = new System.Drawing.Size(680, 325);
			base.Name = "TRApplicationForm";
			Text = "TR Application";
			((System.ComponentModel.ISupportInitialize)numericUpDownTenorDay).EndInit();
			panelTR.ResumeLayout(false);
			panelTR.PerformLayout();
			panelButtons.ResumeLayout(false);
			contextMenuStrip1.ResumeLayout(false);
			panelDetails.ResumeLayout(false);
			panelDetails.PerformLayout();
			((System.ComponentModel.ISupportInitialize)comboBoxVendor).EndInit();
			((System.ComponentModel.ISupportInitialize)comboBoxCostCenter).EndInit();
			((System.ComponentModel.ISupportInitialize)comboBoxSysDoc).EndInit();
			((System.ComponentModel.ISupportInitialize)comboBoxVendorTerm).EndInit();
			panel1.ResumeLayout(false);
			panel1.PerformLayout();
			panelPO.ResumeLayout(false);
			panelPO.PerformLayout();
			((System.ComponentModel.ISupportInitialize)paymentTermComboBox1).EndInit();
			((System.ComponentModel.ISupportInitialize)comboBoxPOTerm).EndInit();
			toolStrip1.ResumeLayout(false);
			toolStrip1.PerformLayout();
			((System.ComponentModel.ISupportInitialize)comboBoxFacility).EndInit();
			ResumeLayout(false);
			PerformLayout();
		}
	}
}
