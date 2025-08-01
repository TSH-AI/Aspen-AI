using Infragistics.Win;
using Infragistics.Win.FormattedLinkLabel;
using Infragistics.Win.Misc;
using Infragistics.Win.UltraWinGrid;
using Infragistics.Win.UltraWinMaskedEdit;
using Micromind.ClientLibraries;
using Micromind.ClientUI.Libraries;
using Micromind.ClientUI.WindowsForms.DataEntries.Customers;
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
	public class ChequePaymentForm : Form, IForm, ITransactionForm, IWorkFlowForm
	{
		private string requestSysDocID = "";

		private TransactionData currentData;

		private const string TABLENAME_CONST = "GL_Transaction";

		private const string IDFIELD_CONST = "VoucherID";

		private bool isNewRecord = true;

		private bool isSameRow = true;

		private bool useJobCosting = CompanyPreferences.UseJobCosting;

		private bool useProperty = CompanyPreferences.UseProperty;

		private string attributeID1Title = CompanyPreferences.AttributeID1Title;

		private string attributeID2Title = CompanyPreferences.AttributeID2Title;

		private bool trackConsignInExpense = CompanyPreferences.TrackConsignInExpense;

		private bool isCostCenterMandatory = CompanyPreferences.IsCostCenterMandatory;

		private bool showAllocationForm = CompanyPreferences.ShowAllocationForm;

		private ScreenAccessRight screenRight;

		private bool ShowSupplierBal;

		private bool ShowCustomerBal;

		private bool ShowAccountBal;

		private bool ShowEmployeeBal;

		private bool AllowEditTransaction;

		private bool AllowEditTransDiffLocation;

		private bool isVoid;

		private string _entityType = string.Empty;

		private decimal _amount;

		private string _entityID = string.Empty;

		private IContainer components;

		private Panel panelButtons;

		private Line linePanelDown;

		private XPButton xpButton1;

		private XPButton buttonSave;

		private FormManager formManager;

		private DataEntryGrid dataGridItems;

		private TextBox textBoxVoucherNumber;

		private Label label1;

		private MMLabel mmLabel1;

		private TextBox textBoxRef1;

		private TextBox textBoxNote;

		private Label label3;

		private CurrencySelector currencySelector;

		private UltraFormattedLinkLabel labelCurrency;

		private AnalysisComboBox comboBoxAnalysis;

		private XPButton buttonDelete;

		private XPButton buttonNew;

		private UltraFormattedLinkLabel ultraFormattedLinkLabel2;

		private UltraLabel ultraLabel1;

		private UltraGroupBox ultraGroupBox1;

		private UltraLabel labelBalance;

		private XPButton buttonVoid;

		private Panel panelDetails;

		private Label labelVoided;

		private UltraFormattedLinkLabel ultraFormattedLinkLabel3;

		private PayeeSelector payeeSelector1;

		private UltraFormattedLinkLabel ultraFormattedLinkLabel4;

		private CostCenterComboBox comboBoxCostCenter;

		private UltraFormattedLinkLabel ultraFormattedLinkLabel5;

		private SysDocComboBox comboBoxSysDoc;

		private TextBox textBoxPayeeName;

		private Label labelAnalysis;

		private flatDatePicker dateTimePickerDate;

		private ChequebookComboBox comboBoxChequebook;

		private CostCategoryComboBox comboBoxCostCategory;

		private JobComboBox comboBoxJob;

		private ExpenseCodeComboBox comboBoxConsignExpense;

		private ConsignInComboBox comboBoxConsignIn;

		private XPButton buttonSelectRequest;

		private UltraFormattedLinkLabel ultraFormattedLinkLabel1;

		private TextBox textBoxRequest;

		private Label label5;

		private TextBox textBoxBalance;

		private MMLabel mmLabel4;

		private AmountTextBox textBoxTotalDue;

		private UltraFormattedLinkLabel ultraFormattedLinkLabel6;

		private Label label2;

		private MMSDateTimePicker dateTimePickerDeliveredDate;

		private UltraFormattedLinkLabel ultraFormattedLinkLabel8;

		private XPButton buttonSelectInvoice;

		private AmountTextBox textBoxAmount;

		private PropertyComboBox comboBoxProperty;

		private PropertyUnitComboBox comboBoxPropertyUnit;

		private DateTimePicker dateTimePickerGrid;

		public ScreenAreas ScreenArea => ScreenAreas.Accounts;

		public int ScreenID => 1011;

		public ScreenTypes ScreenType => ScreenTypes.Transaction;

		public string SystemDocID
		{
			get
			{
				return comboBoxSysDoc.SelectedID;
			}
			set
			{
				comboBoxSysDoc.SelectedID = value;
			}
		}

		public string VoucherID => textBoxVoucherNumber.Text;

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

		public bool IsNewRecord
		{
			get
			{
				return isNewRecord;
			}
			set
			{
				isNewRecord = value;
				if (value)
				{
					buttonNew.Text = UIMessages.ClearButtonText;
					XPButton xPButton = buttonDelete;
					bool enabled = buttonVoid.Enabled = false;
					xPButton.Enabled = enabled;
					textBoxVoucherNumber.Enabled = true;
					comboBoxSysDoc.Enabled = true;
				}
				else
				{
					buttonNew.Text = UIMessages.NewButtonText;
					XPButton xPButton2 = buttonDelete;
					bool enabled = buttonVoid.Enabled = true;
					xPButton2.Enabled = enabled;
					textBoxVoucherNumber.Enabled = false;
					comboBoxSysDoc.Enabled = false;
					buttonSelectInvoice.Enabled = false;
				}
				buttonSelectRequest.Enabled = value;
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
				if (isVoid != value)
				{
					isVoid = value;
					panelDetails.Enabled = !value;
					dataGridItems.Enabled = !value;
					buttonSave.Enabled = !value;
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

		public string EntityType
		{
			private get
			{
				return _entityType;
			}
			set
			{
				_entityType = value;
			}
		}

		public decimal Amount
		{
			private get
			{
				return _amount;
			}
			set
			{
				_amount = value;
			}
		}

		public string EntityID
		{
			private get
			{
				return _entityID;
			}
			set
			{
				_entityID = value;
			}
		}

		public ChequePaymentForm()
		{
			InitializeComponent();
			AddEvents();
			dataGridItems.AllowCustomizeHeaders = true;
		}

		private void AddEvents()
		{
			base.Load += TransactionLeavesForm_Load;
			dataGridItems.CellDataError += dataGrid_CellDataError;
			dataGridItems.BeforeCellUpdate += dataGrid_BeforeCellUpdate;
			dataGridItems.AfterRowActivate += dataGridItems_AfterRowActivate;
			dataGridItems.BeforeRowDeactivate += dataGrid_BeforeRowDeactivate;
			dataGridItems.BeforeCellDeactivate += dataGrid_BeforeCellDeactivate;
			dataGridItems.BeforeCellActivate += dataGridItems_BeforeCellActivate;
			dataGridItems.CellChange += dataGridItems_CellChange;
			dataGridItems.AfterRowsDeleted += dataGridItems_AfterRowsDeleted;
			comboBoxSysDoc.SelectedIndexChanged += comboBoxSysDoc_SelectedIndexChanged;
			comboBoxCostCenter.SelectedIndexChanged += comboBoxCostCenter_SelectedIndexChanged;
			payeeSelector1.SelectedItemChanged += payeeSelector1_SelectedItemChanged;
			comboBoxChequebook.SelectedIndexChanged += comboBoxChequebook_SelectedIndexChanged;
			dataGridItems.AfterCellUpdate += dataGridItems_AfterCellUpdate;
			base.KeyDown += Form_KeyDown;
			base.FormClosing += AccountGroupDetailsForm_FormClosing;
			dataGridItems.BeforeEnterEditMode += dataGridItems_BeforeEnterEditMode;
			base.SizeChanged += dataGridItems_SizeChanged;
			dateTimePickerGrid.Leave += dateTimePicker_Leave;
		}

		private void comboBoxChequebook_SelectedIndexChanged(object sender, EventArgs e)
		{
		}

		private void Form_KeyDown(object sender, KeyEventArgs e)
		{
			if (e.Control && e.KeyCode == Keys.P)
			{
				Print(isPrint: true, showPrintDialog: true, saveChanges: true);
			}
		}

		private void dataGridItems_AfterCellUpdate(object sender, CellEventArgs e)
		{
			if (dataGridItems.ActiveRow == null)
			{
				return;
			}
			checked
			{
				if (e.Cell.Column.Key == "Chequebook")
				{
					if (dataGridItems.ActiveRow.Index > 0 && e.Cell.Value != null && e.Cell.Value.ToString() != "")
					{
						int result = -1;
						for (int num = dataGridItems.ActiveRow.Index - 1; num >= 0; num--)
						{
							if (dataGridItems.Rows[num].Cells["Chequebook"].Value.ToString() == comboBoxChequebook.SelectedID)
							{
								int.TryParse(dataGridItems.Rows[num].Cells["Chq Number"].Value.ToString(), out result);
								break;
							}
						}
						if (result > 0)
						{
							dataGridItems.ActiveRow.Cells["Chq Number"].Value = result + 1;
						}
						else
						{
							try
							{
								dataGridItems.ActiveRow.Cells["Chq Number"].Value = Factory.ChequebookSystem.GetNextChequeNumber(comboBoxChequebook.SelectedID).ToString();
							}
							catch
							{
							}
						}
					}
					else
					{
						try
						{
							dataGridItems.ActiveRow.Cells["Chq Number"].Value = Factory.ChequebookSystem.GetNextChequeNumber(comboBoxChequebook.SelectedID).ToString();
						}
						catch
						{
						}
					}
					dataGridItems.ActiveRow.Cells["Description"].Value = textBoxNote.Text;
					if ((dataGridItems.ActiveRow.Cells["AttributeID1"].Value == null || dataGridItems.ActiveRow.Cells["AttributeID1"].Value.ToString() == "") && dataGridItems.ActiveRow.Index > 0)
					{
						dataGridItems.ActiveRow.Cells["AttributeID1"].Value = dataGridItems.Rows[dataGridItems.ActiveRow.Index - 1].Cells["AttributeID1"].Value;
					}
					if ((dataGridItems.ActiveRow.Cells["AttributeID2"].Value == null || dataGridItems.ActiveRow.Cells["AttributeID2"].Value.ToString() == "") && dataGridItems.ActiveRow.Index > 0)
					{
						dataGridItems.ActiveRow.Cells["AttributeID2"].Value = dataGridItems.Rows[dataGridItems.ActiveRow.Index - 1].Cells["AttributeID2"].Value;
					}
				}
				if (e.Cell.Column.Key == "AttributeID1")
				{
					for (int i = e.Cell.Row.Index + 1; i < dataGridItems.Rows.Count; i++)
					{
						if (dataGridItems.Rows[i].Cells["AttributeID1"].Value.ToString() == "")
						{
							dataGridItems.Rows[i].Cells["AttributeID1"].Value = e.Cell.Value.ToString();
						}
					}
				}
				if (!(e.Cell.Column.Key == "AttributeID2"))
				{
					return;
				}
				for (int j = e.Cell.Row.Index + 1; j < dataGridItems.Rows.Count; j++)
				{
					if (dataGridItems.Rows[j].Cells["AttributeID2"].Value.ToString() == "")
					{
						dataGridItems.Rows[j].Cells["AttributeID2"].Value = e.Cell.Value.ToString();
					}
				}
			}
		}

		private void dataGridItems_BeforeCellListDropDown(object sender, CancelableCellEventArgs e)
		{
			if (e.Cell.Column.ValueList != null && e.Cell.Column.ValueList.GetType().BaseType == typeof(MultiColumnComboBox))
			{
				MultiColumnComboBox multiColumnComboBox = e.Cell.Column.ValueList as MultiColumnComboBox;
				if (e.Cell.Value.ToString() == "")
				{
					multiColumnComboBox.Clear();
				}
				else
				{
					multiColumnComboBox.SelectedID = e.Cell.Value.ToString();
				}
			}
		}

		private void payeeSelector1_SelectedItemChanged(object sender, EventArgs e)
		{
			textBoxPayeeName.Text = payeeSelector1.SelectedName;
			if (payeeSelector1.SelectedType == "V")
			{
				buttonSelectInvoice.Enabled = true;
			}
			else
			{
				buttonSelectInvoice.Enabled = false;
			}
			if (payeeSelector1.SelectedType == "A")
			{
				comboBoxAnalysis.FilterByAccount(payeeSelector1.SelectedID);
				labelAnalysis.Visible = true;
				comboBoxAnalysis.Visible = true;
			}
			else
			{
				comboBoxAnalysis.Clear();
				comboBoxAnalysis.FilterByAccount("$#$$LDF");
				labelAnalysis.Visible = false;
				comboBoxAnalysis.Visible = false;
			}
			if (payeeSelector1.SelectedID != "")
			{
				if (payeeSelector1.SelectedType == "C" && ShowCustomerBal)
				{
					DataSet customerSnapBalance = Factory.CustomerSystem.GetCustomerSnapBalance(payeeSelector1.SelectedID);
					decimal d = decimal.Parse(customerSnapBalance.Tables[0].Rows[0]["Balance"].ToString());
					decimal d2 = decimal.Parse(customerSnapBalance.Tables[0].Rows[0]["PDCAmount"].ToString());
					textBoxBalance.Text = (d - d2).ToString(Format.TotalAmountFormat);
				}
				else if (payeeSelector1.SelectedType == "V" && ShowSupplierBal)
				{
					DataSet vendorBalanceAmount = Factory.VendorSystem.GetVendorBalanceAmount(payeeSelector1.SelectedID);
					decimal d3 = decimal.Parse(vendorBalanceAmount.Tables[0].Rows[0]["Balance"].ToString());
					decimal d4 = decimal.Parse(vendorBalanceAmount.Tables[0].Rows[0]["PDCAmount"].ToString());
					textBoxBalance.Text = (d3 - d4).ToString(Format.TotalAmountFormat);
					decimal num = default(decimal);
					vendorBalanceAmount = Factory.VendorSystem.GetVendorDueBalanceSummary(payeeSelector1.SelectedID, currencySelector.SelectedID, dateTimePickerDate.Value);
					if (vendorBalanceAmount.Tables[0].Rows.Count > 0)
					{
						num = decimal.Parse(vendorBalanceAmount.Tables[0].Rows[0]["BalanceDue"].ToString());
						textBoxTotalDue.Text = num.ToString(Format.TotalAmountFormat);
					}
					if (payeeSelector1.AllowOAP)
					{
						textBoxAmount.ReadOnly = false;
					}
					else
					{
						textBoxAmount.ReadOnly = true;
					}
				}
				else if (payeeSelector1.SelectedType == "E" && ShowEmployeeBal)
				{
					decimal num2 = decimal.Parse(Factory.EmployeeSystem.GetEmployeeSnapBalance(payeeSelector1.SelectedID).Tables[0].Rows[0]["Balance"].ToString());
					textBoxBalance.Text = num2.ToString(Format.TotalAmountFormat);
				}
				else if (payeeSelector1.SelectedType == "A" && ShowAccountBal)
				{
					decimal num3 = decimal.Parse(Factory.JournalSystem.GetAccountSnapBalance(payeeSelector1.SelectedID).Tables[0].Rows[0]["Balance"].ToString());
					textBoxBalance.Text = num3.ToString(Format.TotalAmountFormat);
				}
				else
				{
					textBoxBalance.Text = "";
				}
				if (payeeSelector1.SelectedType == "V")
				{
					bool result = false;
					bool.TryParse(Factory.DatabaseSystem.GetFieldValue("Vendor", "IsHoldForPayment", "VendorID", payeeSelector1.SelectedID).ToString(), out result);
					if (result && IsNewRecord)
					{
						ErrorHelper.WarningMessage("This vendor is on hold status and does not allow transaction.");
						return;
					}
				}
			}
			else
			{
				textBoxBalance.Text = "";
			}
			if (textBoxAmount.Tag != null)
			{
				textBoxAmount.Tag = null;
				textBoxAmount.Clear();
			}
		}

		private void comboBoxCostCenter_SelectedIndexChanged(object sender, EventArgs e)
		{
		}

		private void comboBoxSysDoc_SelectedIndexChanged(object sender, EventArgs e)
		{
			if (isNewRecord)
			{
				textBoxVoucherNumber.Text = GetNextVoucherNumber();
			}
			formManager.SetControlDirtyStatus(textBoxVoucherNumber, textBoxVoucherNumber.Text);
		}

		private void dataGridItems_AfterRowsDeleted(object sender, EventArgs e)
		{
			labelBalance.Text = GetTransactionBalance().ToString(Format.TotalAmountFormat);
		}

		private void dataGridItems_AfterRowActivate(object sender, EventArgs e)
		{
			labelBalance.Text = GetTransactionBalance().ToString(Format.TotalAmountFormat);
			isSameRow = false;
		}

		private void dataGridItems_CellChange(object sender, CellEventArgs e)
		{
			_ = e.Cell.Activated;
		}

		private void dataGridItems_BeforeCellActivate(object sender, CancelableCellEventArgs e)
		{
			if (e.Cell.Column.Key != "Chq Date" && isSameRow)
			{
				dataGridItems.ActiveRow.Cells["Chq Date"].Value = dateTimePickerGrid.Value.ToShortDateString();
				isSameRow = true;
			}
		}

		private void comboBoxGridAccount_SelectedIndexChanged(object sender, EventArgs e)
		{
		}

		private void dataGrid_BeforeCellDeactivate(object sender, CancelEventArgs e)
		{
			if (dataGridItems.ActiveRow != null)
			{
				if (dataGridItems.ActiveCell.Column.Key == "Amount" && dataGridItems.ActiveCell.Text != "")
				{
					dataGridItems.ActiveCell.Value = decimal.Round(decimal.Parse(dataGridItems.ActiveCell.Text, NumberStyles.Any), Global.CurDecimalPoints).ToString(Format.TotalAmountFormat);
				}
				if (dataGridItems.ActiveCell.Column.Key == "Chq Number" && dataGridItems.ActiveCell.Text.Length < 6)
				{
					dataGridItems.ActiveCell.Value = dataGridItems.ActiveCell.Text.PadLeft(6, '0');
				}
			}
		}

		private void dataGrid_BeforeRowDeactivate(object sender, CancelEventArgs e)
		{
			UltraGridRow activeRow = dataGridItems.ActiveRow;
			if (activeRow != null)
			{
				if (activeRow.Cells["Amount"].Value.ToString() == "")
				{
					activeRow.Cells["Amount"].Value = 0;
				}
				if (isSameRow)
				{
					dataGridItems.ActiveRow.Cells["Chq Date"].Value = dateTimePickerGrid.Value.ToShortDateString();
				}
				labelBalance.Text = GetTransactionBalance().ToString(Format.TotalAmountFormat);
			}
		}

		private void dataGrid_BeforeCellUpdate(object sender, BeforeCellUpdateEventArgs e)
		{
			if (e.Cell.Column.Key == "Amount")
			{
				labelBalance.Text = GetTransactionBalance().ToString(Format.TotalAmountFormat);
			}
			if ((e.Cell.Column.Key == "Chequebook" || e.Cell.Column.Key == "Chq Number") && dataGridItems.ActiveRow != null && dataGridItems.Rows.Count > 1)
			{
				string b = dataGridItems.ActiveRow.Cells["Chq Number"].Text.Trim();
				string b2 = dataGridItems.ActiveRow.Cells["Chequebook"].Text.Trim();
				foreach (UltraGridRow row in dataGridItems.Rows)
				{
					if (row != dataGridItems.ActiveRow && row.Cells["Chequebook"].Value.ToString().Trim() == b2 && row.Cells["Chq Number"].Value.ToString().Trim() == b)
					{
						ErrorHelper.WarningMessage(UIMessages.ChequeNumberExist);
						e.Cancel = true;
						break;
					}
				}
			}
		}

		private void dataGrid_CellDataError(object sender, CellDataErrorEventArgs e)
		{
			if (dataGridItems.ActiveCell.Column.Key.ToString() == "Chequebook")
			{
				e.RaiseErrorEvent = false;
				comboBoxChequebook.Text = dataGridItems.ActiveCell.Text;
				comboBoxChequebook.QuickAddItem();
			}
			else if (dataGridItems.ActiveCell.Column.Key.ToString() == "Amount")
			{
				e.RaiseErrorEvent = false;
				ErrorHelper.InformationMessage(UIMessages.InvalidAmount);
			}
		}

		private bool GetData()
		{
			try
			{
				if (currentData == null || isNewRecord)
				{
					currentData = new TransactionData();
				}
				DataRow dataRow = (!isNewRecord) ? currentData.TransactionTable.Rows[0] : currentData.TransactionTable.NewRow();
				dataRow["TransactionID"] = 0;
				dataRow["SysDocType"] = (byte)5;
				dataRow["Description"] = textBoxNote.Text;
				dataRow["CostCenterID"] = comboBoxCostCenter.SelectedID;
				dataRow["TransactionDate"] = dateTimePickerDate.Value;
				dataRow["SysDocID"] = comboBoxSysDoc.SelectedID;
				dataRow["VoucherID"] = textBoxVoucherNumber.Text;
				dataRow["Reference"] = textBoxRef1.Text;
				dataRow["CompanyID"] = Global.CompanyID;
				dataRow["DivisionID"] = comboBoxSysDoc.DivisionID;
				if (dateTimePickerDeliveredDate.Checked)
				{
					dataRow["CheckDeliveredDate"] = dateTimePickerDeliveredDate.Value;
				}
				else
				{
					dataRow["CheckDeliveredDate"] = DBNull.Value;
				}
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
				string text = (string)(dataRow["PayeeType"] = payeeSelector1.SelectedType);
				dataRow["PayeeID"] = payeeSelector1.SelectedID;
				if (currencySelector.SelectedID != "" && currencySelector.SelectedID != Global.BaseCurrencyID)
				{
					dataRow["CurrencyID"] = currencySelector.SelectedID;
					dataRow["CurrencyRate"] = currencySelector.Rate;
					dataRow["AmountFC"] = GetTransactionBalance();
				}
				else
				{
					dataRow["CurrencyID"] = DBNull.Value;
					dataRow["CurrencyRate"] = 1;
					dataRow["Amount"] = GetTransactionBalance();
				}
				if (comboBoxAnalysis.SelectedID != null && comboBoxAnalysis.SelectedID.ToString() != "")
				{
					dataRow["AnalysisID"] = comboBoxAnalysis.SelectedID.ToString();
				}
				else
				{
					dataRow["AnalysisID"] = DBNull.Value;
				}
				dataRow.EndEdit();
				if (IsNewRecord)
				{
					currentData.TransactionTable.Rows.Add(dataRow);
				}
				currentData.TransactionDetailsTable.Rows.Clear();
				foreach (UltraGridRow row in dataGridItems.Rows)
				{
					DataRow dataRow2 = currentData.TransactionDetailsTable.NewRow();
					dataRow2.BeginEdit();
					dataRow2["PaymentMethodType"] = (byte)2;
					dataRow2["ChequebookID"] = row.Cells["Chequebook"].Value.ToString();
					dataRow2["Description"] = row.Cells["Description"].Value.ToString();
					if (currencySelector.SelectedID == "" || currencySelector.IsBaseCurrency)
					{
						if (row.Cells["Amount"].Value.ToString() != "")
						{
							dataRow2["Amount"] = row.Cells["Amount"].Value.ToString();
						}
						else
						{
							dataRow2["Amount"] = DBNull.Value;
						}
						dataRow2["AmountFC"] = DBNull.Value;
					}
					else if (row.Cells["Amount"].Value.ToString() != "")
					{
						dataRow2["AmountFC"] = row.Cells["Amount"].Value.ToString();
					}
					else
					{
						dataRow2["AmountFC"] = DBNull.Value;
					}
					if (row.Cells["Chq Date"].Text != "")
					{
						dataRow2["CheckDate"] = row.Cells["Chq Date"].Value.ToString();
					}
					dataRow2["CheckNumber"] = row.Cells["Chq Number"].Value.ToString();
					if (row.Cells["Job"].Value != null && row.Cells["Job"].Value.ToString() != "")
					{
						dataRow2["JobID"] = row.Cells["Job"].Value.ToString();
					}
					else
					{
						dataRow2["JobID"] = DBNull.Value;
					}
					if (row.Cells["CostCategory"].Value != null && row.Cells["CostCategory"].Value.ToString() != "")
					{
						dataRow2["CostCategoryID"] = row.Cells["CostCategory"].Value.ToString();
					}
					else
					{
						dataRow2["CostCategoryID"] = DBNull.Value;
					}
					if (row.Cells["AttributeID1"].Value != null && row.Cells["AttributeID1"].Value.ToString() != "")
					{
						dataRow2["AttributeID1"] = row.Cells["AttributeID1"].Value.ToString();
					}
					else
					{
						dataRow2["AttributeID1"] = DBNull.Value;
					}
					if (row.Cells["AttributeID2"].Value != null && row.Cells["AttributeID2"].Value.ToString() != "")
					{
						dataRow2["AttributeID2"] = row.Cells["AttributeID2"].Value.ToString();
					}
					else
					{
						dataRow2["AttributeID2"] = DBNull.Value;
					}
					if (row.Cells["Consignment"].Value != null && row.Cells["Consignment"].Value.ToString() != "")
					{
						dataRow2["ConsignID"] = row.Cells["Consignment"].Value.ToString();
					}
					else
					{
						dataRow2["ConsignID"] = DBNull.Value;
					}
					if (row.Cells["ConsignExpenseID"].Value != null && row.Cells["ConsignExpenseID"].Value.ToString() != "")
					{
						dataRow2["ConsignExpenseID"] = row.Cells["ConsignExpenseID"].Value.ToString();
					}
					else
					{
						dataRow2["ConsignExpenseID"] = DBNull.Value;
					}
					dataRow2["RowIndex"] = row.Index;
					dataRow2.EndEdit();
					currentData.TransactionDetailsTable.Rows.Add(dataRow2);
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
					foreach (DataRow row2 in dataSet.Tables["AP_Payment_Advice"].Rows)
					{
						if (!row2["CurrencyID"].IsDBNullOrEmpty())
						{
							a = row2["CurrencyID"].ToString();
						}
						row2["PaymentSysDocID"] = comboBoxSysDoc.SelectedID;
						row2["PaymentVoucherID"] = textBoxVoucherNumber.Text;
						row2["AllocationDate"] = dateTimePickerDate.Value;
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

		private void SetupGrid()
		{
			try
			{
				dataGridItems.DisplayLayout.Bands[0].Columns.ClearUnbound();
				DataTable dataTable = new DataTable();
				dataTable.Columns.Add("Chequebook");
				dataTable.Columns.Add("Chq Number");
				dataTable.Columns.Add("Chq Date", typeof(DateTime));
				dataTable.Columns.Add("Consignment");
				dataTable.Columns.Add("ConsignExpenseID");
				dataTable.Columns.Add("Job");
				dataTable.Columns.Add("CostCategory");
				dataTable.Columns.Add("AttributeID1");
				dataTable.Columns.Add("AttributeID2");
				dataTable.Columns.Add("Description");
				dataTable.Columns.Add("Amount", typeof(decimal));
				dataGridItems.DataSource = dataTable;
				UltraGridColumn ultraGridColumn = dataGridItems.DisplayLayout.Bands[0].Columns["AttributeID1"];
				bool hidden = dataGridItems.DisplayLayout.Bands[0].Columns["AttributeID2"].Hidden = true;
				ultraGridColumn.Hidden = hidden;
				dataGridItems.DisplayLayout.Bands[0].Columns["Chequebook"].Width = checked(7 * dataGridItems.Width) / 100;
				dataGridItems.DisplayLayout.Bands[0].Columns["Chq Number"].Width = checked(7 * dataGridItems.Width) / 100;
				dataGridItems.DisplayLayout.Bands[0].Columns["Amount"].Width = checked(7 * dataGridItems.Width) / 100;
				dataGridItems.DisplayLayout.Bands[0].Columns["Chq Date"].Width = checked(10 * dataGridItems.Width) / 100;
				UltraGridColumn ultraGridColumn2 = dataGridItems.DisplayLayout.Bands[0].Columns["AttributeID1"];
				hidden = (dataGridItems.DisplayLayout.Bands[0].Columns["AttributeID2"].Hidden = !useProperty);
				ultraGridColumn2.Hidden = hidden;
				if (!useProperty)
				{
					ExcludeFromColumnChooser excludeFromColumnChooser3 = dataGridItems.DisplayLayout.Bands[0].Columns["AttributeID1"].ExcludeFromColumnChooser = (dataGridItems.DisplayLayout.Bands[0].Columns["AttributeID1"].ExcludeFromColumnChooser = ExcludeFromColumnChooser.True);
				}
				else
				{
					ExcludeFromColumnChooser excludeFromColumnChooser3 = dataGridItems.DisplayLayout.Bands[0].Columns["AttributeID1"].ExcludeFromColumnChooser = (dataGridItems.DisplayLayout.Bands[0].Columns["AttributeID1"].ExcludeFromColumnChooser = ExcludeFromColumnChooser.False);
				}
				dataGridItems.DisplayLayout.Bands[0].Columns["Chequebook"].CharacterCasing = CharacterCasing.Upper;
				dataGridItems.DisplayLayout.Bands[0].Columns["Chequebook"].MaxLength = 15;
				dataGridItems.DisplayLayout.Bands[0].Columns["Chq Number"].MaxLength = 20;
				dataGridItems.DisplayLayout.Bands[0].Columns["Chequebook"].InvalidValueBehavior = InvalidValueBehavior.RetainValueAndFocus;
				dataGridItems.DisplayLayout.Bands[0].Columns["Chequebook"].Style = Infragistics.Win.UltraWinGrid.ColumnStyle.DropDownValidate;
				dataGridItems.DisplayLayout.Bands[0].Columns["Chequebook"].ValueList = comboBoxChequebook;
				dataGridItems.DisplayLayout.Bands[0].Columns["Chq Date"].Style = Infragistics.Win.UltraWinGrid.ColumnStyle.Date;
				dataGridItems.DisplayLayout.Bands[0].Columns["Job"].Header.Caption = "Project";
				dataGridItems.DisplayLayout.Bands[0].Columns["Job"].CharacterCasing = CharacterCasing.Upper;
				dataGridItems.DisplayLayout.Bands[0].Columns["Job"].MaxLength = 64;
				dataGridItems.DisplayLayout.Bands[0].Columns["Job"].Width = 75;
				dataGridItems.DisplayLayout.Bands[0].Columns["Job"].InvalidValueBehavior = InvalidValueBehavior.RetainValueAndFocus;
				dataGridItems.DisplayLayout.Bands[0].Columns["Job"].Style = Infragistics.Win.UltraWinGrid.ColumnStyle.DropDownValidate;
				dataGridItems.DisplayLayout.Bands[0].Columns["Job"].ValueList = comboBoxJob;
				dataGridItems.DisplayLayout.Bands[0].Columns["CostCategory"].Header.Caption = "Cost Category";
				dataGridItems.DisplayLayout.Bands[0].Columns["CostCategory"].CharacterCasing = CharacterCasing.Upper;
				dataGridItems.DisplayLayout.Bands[0].Columns["CostCategory"].MaxLength = 64;
				dataGridItems.DisplayLayout.Bands[0].Columns["CostCategory"].Width = 75;
				dataGridItems.DisplayLayout.Bands[0].Columns["CostCategory"].InvalidValueBehavior = InvalidValueBehavior.RetainValueAndFocus;
				dataGridItems.DisplayLayout.Bands[0].Columns["CostCategory"].Style = Infragistics.Win.UltraWinGrid.ColumnStyle.DropDownValidate;
				dataGridItems.DisplayLayout.Bands[0].Columns["CostCategory"].ValueList = comboBoxCostCategory;
				dataGridItems.DisplayLayout.Bands[0].Columns["AttributeID1"].Header.Caption = attributeID1Title;
				dataGridItems.DisplayLayout.Bands[0].Columns["AttributeID1"].CharacterCasing = CharacterCasing.Upper;
				dataGridItems.DisplayLayout.Bands[0].Columns["AttributeID1"].MaxLength = 64;
				dataGridItems.DisplayLayout.Bands[0].Columns["AttributeID1"].Width = 75;
				dataGridItems.DisplayLayout.Bands[0].Columns["AttributeID1"].InvalidValueBehavior = InvalidValueBehavior.RetainValueAndFocus;
				dataGridItems.DisplayLayout.Bands[0].Columns["AttributeID1"].Style = Infragistics.Win.UltraWinGrid.ColumnStyle.DropDownValidate;
				dataGridItems.DisplayLayout.Bands[0].Columns["AttributeID1"].ValueList = comboBoxProperty;
				dataGridItems.DisplayLayout.Bands[0].Columns["AttributeID2"].Header.Caption = attributeID2Title;
				dataGridItems.DisplayLayout.Bands[0].Columns["AttributeID2"].CharacterCasing = CharacterCasing.Upper;
				dataGridItems.DisplayLayout.Bands[0].Columns["AttributeID2"].MaxLength = 64;
				dataGridItems.DisplayLayout.Bands[0].Columns["AttributeID2"].Width = 75;
				dataGridItems.DisplayLayout.Bands[0].Columns["AttributeID2"].InvalidValueBehavior = InvalidValueBehavior.RetainValueAndFocus;
				dataGridItems.DisplayLayout.Bands[0].Columns["AttributeID2"].Style = Infragistics.Win.UltraWinGrid.ColumnStyle.DropDownValidate;
				dataGridItems.DisplayLayout.Bands[0].Columns["AttributeID2"].ValueList = comboBoxPropertyUnit;
				dataGridItems.DisplayLayout.Bands[0].Columns["Consignment"].CharacterCasing = CharacterCasing.Upper;
				dataGridItems.DisplayLayout.Bands[0].Columns["Consignment"].MaxLength = 22;
				dataGridItems.DisplayLayout.Bands[0].Columns["Consignment"].Width = 75;
				dataGridItems.DisplayLayout.Bands[0].Columns["Consignment"].InvalidValueBehavior = InvalidValueBehavior.RetainValueAndFocus;
				dataGridItems.DisplayLayout.Bands[0].Columns["Consignment"].Style = Infragistics.Win.UltraWinGrid.ColumnStyle.DropDownValidate;
				dataGridItems.DisplayLayout.Bands[0].Columns["Consignment"].ValueList = comboBoxConsignIn;
				dataGridItems.DisplayLayout.Bands[0].Columns["ConsignExpenseID"].Header.Caption = "Expense Category";
				dataGridItems.DisplayLayout.Bands[0].Columns["ConsignExpenseID"].CharacterCasing = CharacterCasing.Upper;
				dataGridItems.DisplayLayout.Bands[0].Columns["ConsignExpenseID"].MaxLength = 64;
				dataGridItems.DisplayLayout.Bands[0].Columns["ConsignExpenseID"].Width = 75;
				dataGridItems.DisplayLayout.Bands[0].Columns["ConsignExpenseID"].InvalidValueBehavior = InvalidValueBehavior.RetainValueAndFocus;
				dataGridItems.DisplayLayout.Bands[0].Columns["ConsignExpenseID"].Style = Infragistics.Win.UltraWinGrid.ColumnStyle.DropDownValidate;
				dataGridItems.DisplayLayout.Bands[0].Columns["ConsignExpenseID"].ValueList = comboBoxConsignExpense;
				UltraGridColumn ultraGridColumn3 = dataGridItems.DisplayLayout.Bands[0].Columns["Job"];
				hidden = (dataGridItems.DisplayLayout.Bands[0].Columns["CostCategory"].Hidden = !useJobCosting);
				ultraGridColumn3.Hidden = hidden;
				if (!useJobCosting)
				{
					ExcludeFromColumnChooser excludeFromColumnChooser3 = dataGridItems.DisplayLayout.Bands[0].Columns["Job"].ExcludeFromColumnChooser = (dataGridItems.DisplayLayout.Bands[0].Columns["CostCategory"].ExcludeFromColumnChooser = ExcludeFromColumnChooser.True);
				}
				else
				{
					ExcludeFromColumnChooser excludeFromColumnChooser3 = dataGridItems.DisplayLayout.Bands[0].Columns["Job"].ExcludeFromColumnChooser = (dataGridItems.DisplayLayout.Bands[0].Columns["CostCategory"].ExcludeFromColumnChooser = ExcludeFromColumnChooser.False);
				}
				UltraGridColumn ultraGridColumn4 = dataGridItems.DisplayLayout.Bands[0].Columns["Consignment"];
				hidden = (dataGridItems.DisplayLayout.Bands[0].Columns["ConsignExpenseID"].Hidden = !trackConsignInExpense);
				ultraGridColumn4.Hidden = hidden;
				if (!trackConsignInExpense)
				{
					ExcludeFromColumnChooser excludeFromColumnChooser3 = dataGridItems.DisplayLayout.Bands[0].Columns["Consignment"].ExcludeFromColumnChooser = (dataGridItems.DisplayLayout.Bands[0].Columns["ConsignExpenseID"].ExcludeFromColumnChooser = ExcludeFromColumnChooser.True);
				}
				else
				{
					ExcludeFromColumnChooser excludeFromColumnChooser3 = dataGridItems.DisplayLayout.Bands[0].Columns["Consignment"].ExcludeFromColumnChooser = (dataGridItems.DisplayLayout.Bands[0].Columns["ConsignExpenseID"].ExcludeFromColumnChooser = ExcludeFromColumnChooser.False);
				}
				dataGridItems.DisplayLayout.Bands[0].Columns["Amount"].MinValue = 0;
				dataGridItems.DisplayLayout.Bands[0].Columns["Amount"].MaxValue = new decimal(999999999999L);
				dataGridItems.DisplayLayout.Bands[0].Columns["Amount"].CellAppearance.TextHAlign = HAlign.Right;
				dataGridItems.DisplayLayout.Bands[0].Columns["Amount"].Format = Format.TotalAmountFormat;
				dataGridItems.DisplayLayout.Bands[0].Columns["Description"].MaxLength = 255;
			}
			catch (Exception e)
			{
				dataGridItems.LoadLayoutFailed = true;
				ErrorHelper.ProcessError(e);
			}
		}

		private void buttonSave_Click(object sender, EventArgs e)
		{
			SaveData();
			dataGridItems.Focus();
		}

		public void LoadData(string journalID)
		{
			try
			{
				if (!(journalID.Trim() == "") && CanClose())
				{
					currentData = Factory.TransactionSystem.GetTransactionByID(SystemDocID, journalID);
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
				if (currentData != null && currentData.Tables.Count != 0 && currentData.Tables[0].Rows.Count != 0)
				{
					DataRow dataRow = currentData.Tables["GL_Transaction"].Rows[0];
					dateTimePickerDate.Value = DateTime.Parse(dataRow["TransactionDate"].ToString());
					textBoxVoucherNumber.Text = dataRow["VoucherID"].ToString();
					textBoxRef1.Text = dataRow["Reference"].ToString();
					comboBoxCostCenter.SelectedID = dataRow["CostCenterID"].ToString();
					textBoxNote.Text = dataRow["Description"].ToString();
					payeeSelector1.SelectedType = dataRow["PayeeType"].ToString();
					payeeSelector1.SelectedID = dataRow["PayeeID"].ToString();
					comboBoxAnalysis.SelectedID = dataRow["AnalysisID"].ToString();
					requestSysDocID = dataRow["RequestSysDocID"].ToString();
					textBoxRequest.Text = dataRow["RequestVoucherID"].ToString();
					if (dataRow["CheckDeliveredDate"] != DBNull.Value)
					{
						dateTimePickerDeliveredDate.Value = DateTime.Parse(dataRow["CheckDeliveredDate"].ToString());
						dateTimePickerDeliveredDate.Checked = true;
					}
					else
					{
						dateTimePickerDeliveredDate.Clear();
					}
					if (textBoxRequest.Text != "")
					{
						payeeSelector1.Enabled = false;
						comboBoxChequebook.Enabled = false;
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
					if (dataRow["IsVoid"] != DBNull.Value)
					{
						IsVoid = bool.Parse(dataRow["IsVoid"].ToString());
					}
					else
					{
						IsVoid = false;
					}
					if (dataRow["AnalysisID"] != DBNull.Value)
					{
						comboBoxAnalysis.SelectedID = dataRow["AnalysisID"].ToString();
					}
					else
					{
						comboBoxAnalysis.Clear();
					}
					DataTable dataTable = dataGridItems.DataSource as DataTable;
					dataTable.Rows.Clear();
					if (currentData.Tables.Contains("Transaction_Details") && currentData.TransactionDetailsTable.Rows.Count != 0)
					{
						foreach (DataRow row in currentData.Tables["Transaction_Details"].Rows)
						{
							DataRow dataRow3 = dataTable.NewRow();
							dataRow3["Chequebook"] = row["ChequebookID"];
							dataRow3["Chq Number"] = row["CheckNumber"];
							dataRow3["Chq Date"] = row["CheckDate"];
							if (row["AmountFC"] != DBNull.Value)
							{
								dataRow3["Amount"] = Math.Round(decimal.Parse(row["AmountFC"].ToString()), Global.CurDecimalPoints);
							}
							else if (row["Amount"] != DBNull.Value)
							{
								dataRow3["Amount"] = Math.Round(decimal.Parse(row["Amount"].ToString()), Global.CurDecimalPoints);
							}
							else
							{
								dataRow3["Amount"] = DBNull.Value;
							}
							if (row["JobID"] != DBNull.Value)
							{
								dataRow3["Job"] = row["JobID"];
							}
							if (row["CostCategoryID"] != DBNull.Value)
							{
								dataRow3["CostCategory"] = row["CostCategoryID"];
							}
							if (row["AttributeID1"] != DBNull.Value)
							{
								dataRow3["AttributeID1"] = row["AttributeID1"];
							}
							if (row["AttributeID2"] != DBNull.Value)
							{
								dataRow3["AttributeID2"] = row["AttributeID2"];
							}
							if (row["ConsignID"] != DBNull.Value)
							{
								dataRow3["Consignment"] = row["ConsignID"];
							}
							if (row["ConsignExpenseID"] != DBNull.Value)
							{
								dataRow3["ConsignExpenseID"] = row["ConsignExpenseID"];
							}
							dataRow3["Description"] = row["Description"].ToString();
							dataRow3.EndEdit();
							dataTable.Rows.Add(dataRow3);
						}
						dataTable.AcceptChanges();
						foreach (UltraGridRow row2 in dataGridItems.Rows)
						{
							if (row2.Cells["Chq Date"].Value == DBNull.Value)
							{
								row2.Cells["Chq Date"].Activation = Activation.Disabled;
							}
							else
							{
								row2.Cells["Chq Date"].Activation = Activation.AllowEdit;
							}
						}
						if (currentData.Tables["Cheque_Issued"].Select("Status>2").Length != 0)
						{
							foreach (UltraGridColumn column in dataGridItems.DisplayLayout.Bands[0].Columns)
							{
								column.CellActivation = Activation.NoEdit;
							}
							dataGridItems.ShowDeleteMenu = false;
							dataGridItems.AllowAddNew = false;
							foreach (UltraGridRow row3 in dataGridItems.Rows)
							{
								row3.Appearance.BackColor = Color.WhiteSmoke;
							}
							payeeSelector1.Enabled = false;
						}
						else
						{
							foreach (UltraGridColumn column2 in dataGridItems.DisplayLayout.Bands[0].Columns)
							{
								column2.CellActivation = Activation.AllowEdit;
							}
							dataGridItems.ShowDeleteMenu = true;
							dataGridItems.AllowAddNew = true;
							if (textBoxRequest.Text == "")
							{
								payeeSelector1.Enabled = true;
							}
						}
						labelBalance.Text = GetTransactionBalance().ToString(Format.TotalAmountFormat);
						if (currentData.Tables["AP_Payment_Advice"].Rows.Count > 0)
						{
							textBoxAmount.Tag = currentData;
							textBoxAmount.ReadOnly = true;
						}
					}
				}
			}
			catch
			{
				throw;
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
				bool flag2 = (!isNewRecord) ? Factory.TransactionSystem.UpdateTransaction(currentData) : Factory.TransactionSystem.CreateTransaction(currentData);
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
					if (showAllocationForm && textBoxAmount.Tag == null && payeeSelector1.SelectedType == "V")
					{
						CustomerPaymentAllocationForm customerPaymentAllocationForm = new CustomerPaymentAllocationForm();
						customerPaymentAllocationForm.IsARPayment = false;
						customerPaymentAllocationForm.SetData(comboBoxSysDoc.SelectedID, textBoxVoucherNumber.Text, payeeSelector1.SelectedID, -1, isPDC: false);
						customerPaymentAllocationForm.ShowDialog();
					}
					bool result = false;
					bool result2 = false;
					bool.TryParse(comboBoxSysDoc.GetSelectedCellValue("DoPrint").ToString(), out result);
					if (result)
					{
						bool.TryParse(comboBoxSysDoc.GetSelectedCellValue("PrintAfterSave").ToString(), out result2);
						if (result2)
						{
							Print(isPrint: true, showPrintDialog: true, saveChanges: false);
						}
						else
						{
							Print(isPrint: false, showPrintDialog: true, saveChanges: false);
						}
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
				if (ex.Number == 2006)
				{
					ErrorHelper.WarningMessage(ex.Message);
				}
				else
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
				}
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
			if (!IsNewRecord && !Global.IsUserAdmin && !AllowEditTransaction && Global.CurrentUser != Factory.SystemDocumentSystem.GetTransUserID("GL_Transaction", "VoucherID", SystemDocID, textBoxVoucherNumber.Text))
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
			if (payeeSelector1.SelectedType == "V" && payeeSelector1.SelectedID != "")
			{
				bool result = false;
				bool.TryParse(Factory.DatabaseSystem.GetFieldValue("Vendor", "IsHoldForPayment", "VendorID", payeeSelector1.SelectedID).ToString(), out result);
				if (result && IsNewRecord)
				{
					ErrorHelper.WarningMessage("This vendor is on hold status and does not allow transaction.");
					return false;
				}
			}
			if (comboBoxSysDoc.SelectedID == "" || textBoxVoucherNumber.Text.Trim() == "" || payeeSelector1.SelectedID == "")
			{
				ErrorHelper.InformationMessage(UIMessages.EnterRequiredFields);
				return false;
			}
			if (isCostCenterMandatory && comboBoxCostCenter.SelectedID == string.Empty)
			{
				ErrorHelper.InformationMessage("Please select cost center");
				return false;
			}
			decimal d = default(decimal);
			foreach (UltraGridRow row in dataGridItems.Rows)
			{
				if (!dataGridItems.HasRowAnyValue(row))
				{
					row.Delete(displayPrompt: false);
				}
				else if (row.Cells["Chq Date"].Activation == Activation.AllowEdit)
				{
					if (row.Cells["Chequebook"].Value.ToString().Trim() == "")
					{
						ErrorHelper.InformationMessage(UIMessages.SelectAChequebook);
						row.Activate();
						return false;
					}
					if (row.Cells["Chq Number"].Value.ToString().Trim() == "")
					{
						ErrorHelper.InformationMessage(UIMessages.EnterChequeNumber);
						row.Activate();
						return false;
					}
					int result2 = 0;
					if (!int.TryParse(row.Cells["Chq Number"].Value.ToString(), out result2))
					{
						ErrorHelper.InformationMessage("Cheque numbers must be numeric value. Please enter a numeric value for the cheque numbers.");
						row.Activate();
						return false;
					}
					if (row.Cells["Chq Date"].Value.ToString() == "")
					{
						ErrorHelper.InformationMessage(UIMessages.EnterChequeDate);
						row.Activate();
						return false;
					}
					if (row.Cells["Amount"].Value.ToString() == "")
					{
						ErrorHelper.InformationMessage(UIMessages.EnterChequeAmount);
						row.Activate();
						return false;
					}
				}
				d += decimal.Parse(row.Cells["Amount"].Value.ToString());
			}
			decimal num = decimal.Parse(textBoxAmount.Text);
			if (textBoxAmount.Tag != null)
			{
				if (payeeSelector1.AllowOAP && num != 0m && d != num)
				{
					ErrorHelper.WarningMessage("Total bills selected to pay must be equal to total payment amount.");
					return false;
				}
				if (!payeeSelector1.AllowOAP && d != num)
				{
					ErrorHelper.WarningMessage("Total bills selected to pay must be equal to total payment amount.");
					return false;
				}
			}
			if (dataGridItems.Rows.Count == 0)
			{
				ErrorHelper.InformationMessage(UIMessages.EnterAtLeastOneRowOfPayment);
				return false;
			}
			if (GetTransactionBalance() == 0m && ErrorHelper.QuestionMessageYesNo(UIMessages.TransactionWithZeroAmount) == DialogResult.No)
			{
				return false;
			}
			try
			{
				foreach (UltraGridRow row2 in dataGridItems.Rows)
				{
					int num2 = (!isNewRecord) ? Factory.IssuedChequeSystem.ValidateBlankCheque(row2.Cells["Chequebook"].Value.ToString(), row2.Cells["Chq Number"].Value.ToString(), comboBoxSysDoc.SelectedID, textBoxVoucherNumber.Text) : Factory.IssuedChequeSystem.ValidateBlankCheque(row2.Cells["Chequebook"].Value.ToString(), row2.Cells["Chq Number"].Value.ToString(), "", "");
					if (num2 < 0)
					{
						switch (num2)
						{
						case -1:
							ErrorHelper.InformationMessage(UIMessages.ChequeNotRegistered);
							row2.Activate();
							return false;
						case -2:
							ErrorHelper.InformationMessage(UIMessages.ChequeInUseNotBlank);
							row2.Activate();
							return false;
						default:
							ErrorHelper.InformationMessage(UIMessages.InvalidChequeNumber);
							row2.Activate();
							return false;
						}
					}
				}
			}
			catch (Exception e)
			{
				ErrorHelper.ProcessError(e);
			}
			if (formManager.IsFieldDirty(textBoxVoucherNumber) && Factory.SystemDocumentSystem.ExistDocumentNumber("GL_Transaction", "VoucherID", SystemDocID, textBoxVoucherNumber.Text))
			{
				ErrorHelper.WarningMessage(UIMessages.DocumentNumberInUse);
				textBoxVoucherNumber.Focus();
				return false;
			}
			return true;
		}

		private decimal GetTransactionBalance()
		{
			decimal result = default(decimal);
			foreach (UltraGridRow row in dataGridItems.Rows)
			{
				if (row.Cells["Amount"].Value != null && row.Cells["Amount"].Value.ToString() != "")
				{
					result += decimal.Parse(row.Cells["Amount"].Value.ToString());
				}
			}
			return result;
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
				textBoxNote.Clear();
				textBoxRef1.Clear();
				dateTimePickerDate.Value = DateTime.Now;
				buttonSelectInvoice.Enabled = true;
				textBoxAmount.Tag = null;
				textBoxAmount.ReadOnly = false;
				textBoxAmount.Clear();
				textBoxVoucherNumber.Text = GetNextVoucherNumber();
				comboBoxAnalysis.Clear();
				payeeSelector1.Clear();
				textBoxPayeeName.Clear();
				labelBalance.Text = GetTransactionBalance().ToString(Format.TotalAmountFormat);
				labelBalance.Text = 0.ToString(Format.TotalAmountFormat);
				textBoxRequest.Clear();
				requestSysDocID = "";
				payeeSelector1.Enabled = true;
				comboBoxChequebook.Enabled = true;
				dateTimePickerDeliveredDate.Clear();
				dataGridItems.AllowAddNew = true;
				foreach (UltraGridColumn column in dataGridItems.DisplayLayout.Bands[0].Columns)
				{
					column.CellActivation = Activation.AllowEdit;
				}
				if (payeeSelector1.SelectedType == "")
				{
					payeeSelector1.SelectedType = "V";
				}
				comboBoxSysDoc.SetDefaultID(Security.DefaultTransactionLocationID);
				(dataGridItems.DataSource as DataTable).Rows.Clear();
				(base.ParentForm as IWorkFlowForm)?.SetApprovalStatus();
				EventHelper.OnFormCleared(this, null);
				IsVoid = false;
				formManager.ResetDirty();
				dateTimePickerDate.Focus();
			}
			catch (Exception e)
			{
				ErrorHelper.ProcessError(e);
			}
		}

		private void TransactionLeaveGroupDetailsForm_Validating(object sender, CancelEventArgs e)
		{
		}

		private void TransactionLeaveGroupDetailsForm_Validated(object sender, EventArgs e)
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
				if (ErrorHelper.QuestionMessageYesNo(UIMessages.DeleteRecord) == DialogResult.No)
				{
					return false;
				}
				return Factory.TransactionSystem.DeleteTransaction(SystemDocID, textBoxVoucherNumber.Text);
			}
			catch (Exception e)
			{
				ErrorHelper.ProcessError(e);
				return false;
			}
		}

		private void xpButton1_Click(object sender, EventArgs e)
		{
		}

		private void toolStripButtonNext_Click(object sender, EventArgs e)
		{
			string nextID = DatabaseHelper.GetNextID("GL_Transaction", "VoucherID", textBoxVoucherNumber.Text, "SysDocID", SystemDocID);
			if (!(nextID == ""))
			{
				LoadData(nextID);
			}
		}

		private void toolStripButtonPrevious_Click(object sender, EventArgs e)
		{
			string previousID = DatabaseHelper.GetPreviousID("GL_Transaction", "VoucherID", textBoxVoucherNumber.Text, "SysDocID", SystemDocID);
			if (!(previousID == ""))
			{
				LoadData(previousID);
			}
		}

		private void GoLast()
		{
			string lastID = DatabaseHelper.GetLastID("GL_Transaction", "VoucherID", "SysDocID", SystemDocID);
			if (!(lastID == ""))
			{
				LoadData(lastID);
			}
		}

		private void GoFirst()
		{
			string firstID = DatabaseHelper.GetFirstID("GL_Transaction", "VoucherID", "SysDocID", SystemDocID);
			if (!(firstID == ""))
			{
				LoadData(firstID);
			}
		}

		private void toolStripButtonFind_Click(object sender, EventArgs e)
		{
		}

		public void OnActivated()
		{
		}

		private void AccountGroupDetailsForm_FormClosing(object sender, FormClosingEventArgs e)
		{
			if (!CanClose())
			{
				e.Cancel = true;
			}
			else
			{
				dataGridItems.SaveLayout();
			}
		}

		public bool CanClose()
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

		private void TransactionLeavesForm_Load(object sender, EventArgs e)
		{
			try
			{
				dataGridItems.SetupUI();
				SetupGrid();
				dataGridItems.ApplyFormat();
				UltraFormattedLinkLabel ultraFormattedLinkLabel = labelCurrency;
				bool visible = currencySelector.Visible = CompanyPreferences.UseMultiCurrency;
				ultraFormattedLinkLabel.Visible = visible;
				SetSecurity();
				if (!base.IsDisposed)
				{
					dateTimePickerDate.Value = DateTime.Now;
					IsNewRecord = true;
					comboBoxSysDoc.FilterByType(SysDocTypes.ChequePayment);
					LoadDataIfExist();
					dataGridItems.DisplayLayout.Bands[0].Columns["Chq Date"].FormatInfo = CultureInfo.CurrentCulture;
					dataGridItems.DisplayLayout.Bands[0].Columns["Chq Date"].Format = "d";
					dataGridItems.DisplayLayout.Bands[0].Columns["Chq Date"].MaskDisplayMode = MaskMode.IncludeBoth;
					dataGridItems.DisplayLayout.Bands[0].Columns["Chq Date"].Style = Infragistics.Win.UltraWinGrid.ColumnStyle.Date;
					ClearForm();
				}
			}
			catch (Exception e2)
			{
				dataGridItems.LoadLayoutFailed = true;
				ErrorHelper.ProcessError(e2);
			}
		}

		private void LoadDataIfExist()
		{
			payeeSelector1.SelectedType = EntityType;
			payeeSelector1.SelectedID = EntityID;
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
			if (!Security.IsAllowedSecurityRole(GeneralSecurityRoles.AccessSupplierBal))
			{
				ShowSupplierBal = false;
			}
			else
			{
				ShowSupplierBal = true;
			}
			if (!Security.IsAllowedSecurityRole(GeneralSecurityRoles.AccessCustomerBal))
			{
				ShowCustomerBal = false;
			}
			else
			{
				ShowCustomerBal = true;
			}
			if (!Security.IsAllowedSecurityRole(GeneralSecurityRoles.AccessAccountBal))
			{
				ShowAccountBal = false;
			}
			else
			{
				ShowAccountBal = true;
			}
			if (!Security.IsAllowedSecurityRole(GeneralSecurityRoles.AccessEmployeeBal))
			{
				ShowEmployeeBal = false;
			}
			else
			{
				ShowEmployeeBal = true;
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

		private void dataGridItems_AfterCellActivate(object sender, EventArgs e)
		{
			if (dataGridItems.ActiveRow != null)
			{
				_ = dataGridItems.ActiveCell;
			}
		}

		private void ultraFormattedLinkLabel1_LinkClicked(object sender, Infragistics.Win.FormattedLinkLabel.LinkClickedEventArgs e)
		{
			new FormHelper().EditCurrency(currencySelector.SelectedID);
		}

		private void ultraFormattedLinkLabel2_LinkClicked(object sender, Infragistics.Win.FormattedLinkLabel.LinkClickedEventArgs e)
		{
			textBoxVoucherNumber.Text = GetNextVoucherNumber();
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
				return Factory.TransactionSystem.VoidTransaction(SystemDocID, textBoxVoucherNumber.Text, isVoid);
			}
			catch (Exception e)
			{
				ErrorHelper.ProcessError(e);
				return false;
			}
		}

		private void ultraFormattedLinkLabel3_LinkClicked(object sender, Infragistics.Win.FormattedLinkLabel.LinkClickedEventArgs e)
		{
			string selectedType = payeeSelector1.SelectedType;
			if (!(selectedType == ""))
			{
				FormHelper formHelper = new FormHelper();
				if (selectedType == "A")
				{
					formHelper.EditAccount(payeeSelector1.SelectedID);
				}
				else if (selectedType == "C")
				{
					formHelper.EditCustomer(payeeSelector1.SelectedID);
				}
				else if (selectedType == "V")
				{
					formHelper.EditVendor(payeeSelector1.SelectedID);
				}
				else if (selectedType == "E")
				{
					formHelper.EditEmployee(payeeSelector1.SelectedID);
				}
			}
		}

		private void ultraFormattedLinkLabel4_LinkClicked(object sender, Infragistics.Win.FormattedLinkLabel.LinkClickedEventArgs e)
		{
			new FormHelper().EditCostCenter(comboBoxCostCenter.SelectedID);
		}

		private void ultraFormattedLinkLabel5_LinkClicked(object sender, Infragistics.Win.FormattedLinkLabel.LinkClickedEventArgs e)
		{
			new FormHelper().EditSysDoc(comboBoxSysDoc.SelectedID, SysDocTypes.ChequePayment);
		}

		private void toolStripButtonPrint_Click(object sender, EventArgs e)
		{
			Print(isPrint: true, showPrintDialog: true, saveChanges: true);
		}

		public void Print()
		{
			Print(isPrint: true, showPrintDialog: true, saveChanges: true);
		}

		private void Print(bool isPrint, bool showPrintDialog, bool saveChanges)
		{
			try
			{
				if (!(IsDirty && saveChanges) || (ErrorHelper.QuestionMessage(MessageBoxButtons.YesNo, "You must save the document before printing.", "Do you want to save?") == DialogResult.Yes && SaveData(clearAfter: false)))
				{
					string systemDocID = SystemDocID;
					string text = textBoxVoucherNumber.Text;
					DataSet transactionToPrint = Factory.TransactionSystem.GetTransactionToPrint(systemDocID, text);
					if (transactionToPrint == null || transactionToPrint.Tables.Count == 0)
					{
						ErrorHelper.ErrorMessage("Cannot print the document.", "Document not found.");
					}
					else
					{
						PrintHelper.PrintDocument(transactionToPrint, systemDocID, "Cheque Payment", SysDocTypes.ChequePayment, isPrint, showPrintDialog);
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
			Preview();
		}

		public void Preview()
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

		private void toolStripButtonOpenList_Click(object sender, EventArgs e)
		{
			FormActivator.BringFormToFront(FormActivator.PaymentVoucherListObj);
		}

		private void toolStripButtonAttach_Click(object sender, EventArgs e)
		{
			try
			{
				if (!isNewRecord)
				{
					DocManagementForm docManagementForm = new DocManagementForm();
					if (!(comboBoxSysDoc.SelectedID == "") || !(textBoxVoucherNumber.Text.Trim() == ""))
					{
						docManagementForm.EntityID = textBoxVoucherNumber.Text.Trim();
						docManagementForm.EntitySysDocID = comboBoxSysDoc.SelectedID;
						docManagementForm.EntityName = comboBoxSysDoc.SelectedID;
						docManagementForm.EntityType = EntityTypesEnum.Transactions;
						docManagementForm.ShowDialog(this);
					}
				}
			}
			catch (Exception e2)
			{
				ErrorHelper.ProcessError(e2);
			}
		}

		public void SetApprovalStatus()
		{
		}

		public void ShowForApproval(string sysDocID, string voucherID, int approvalTaskID)
		{
			EditDocument(sysDocID, voucherID);
			formManager.ShowApprovalPanel(approvalTaskID, "GL_Transaction", "VoucherID");
		}

		private void toolStripButtonDistribution_Click(object sender, EventArgs e)
		{
			JournalDistibutionDialog journalDistibutionDialog = new JournalDistibutionDialog();
			journalDistibutionDialog.VoucherID = textBoxVoucherNumber.Text;
			journalDistibutionDialog.SysDocID = comboBoxSysDoc.SelectedID;
			journalDistibutionDialog.ShowDialog(this);
		}

		private void buttonSelectInvoice_Click(object sender, EventArgs e)
		{
			string vendorID = "";
			if (payeeSelector1.SelectedType == "V")
			{
				vendorID = payeeSelector1.SelectedID;
			}
			SelectInvoicesToPay(vendorID, payeeSelector1.SelectedName, currencySelector.SelectedID);
		}

		private void ultraFormattedLinkLabel8_LinkClicked(object sender, Infragistics.Win.FormattedLinkLabel.LinkClickedEventArgs e)
		{
			DataSet dataSet = null;
			if (textBoxAmount.Tag != null)
			{
				dataSet = (textBoxAmount.Tag as DataSet);
				PaymentAdviceDetailsForm paymentAdviceDetailsForm = new PaymentAdviceDetailsForm();
				paymentAdviceDetailsForm.SetData(payeeSelector1.SelectedID, payeeSelector1.SelectedName, currencySelector.SelectedID, currencySelector.Rate);
				paymentAdviceDetailsForm.PaymentData = dataSet;
				paymentAdviceDetailsForm.IsViewOnly = true;
				paymentAdviceDetailsForm.ShowDialog();
			}
		}

		private void buttonSelectRequest_Click(object sender, EventArgs e)
		{
			try
			{
				DataSet openPaymentRequests = Factory.PaymentRequestSystem.GetOpenPaymentRequests(1);
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
						payeeSelector1.SelectedType = "V";
						payeeSelector1.SelectedID = dataRow["PayeeID"].ToString();
						comboBoxChequebook.SelectedID = dataRow["PayFromID"].ToString();
						currencySelector.SelectedID = dataRow["CurrencyID"].ToString();
						payeeSelector1.Enabled = false;
						comboBoxChequebook.Enabled = false;
					}
				}
			}
			catch (Exception e2)
			{
				ErrorHelper.ProcessError(e2);
			}
		}

		private void ultraFormattedLinkLabel1_LinkClicked_1(object sender, Infragistics.Win.FormattedLinkLabel.LinkClickedEventArgs e)
		{
			new FormHelper().EditTransaction(TransactionListType.PaymentRequest, requestSysDocID, textBoxRequest.Text);
		}

		private void ultraFormattedLinkLabel6_LinkClicked(object sender, Infragistics.Win.FormattedLinkLabel.LinkClickedEventArgs e)
		{
			try
			{
				if (dataGridItems.ActiveRow != null && currentData != null && dataGridItems.ActiveRow.Cells["Chq Number"].Value != null && dataGridItems.ActiveRow.Cells["Chq Number"].Value.ToString() != "")
				{
					string text = "";
					string text2 = "";
					int index = dataGridItems.ActiveRow.Index;
					text = currentData.Tables["Cheque_Issued"].Rows[index]["ClearanceSysDocID"].ToString();
					text2 = currentData.Tables["Cheque_Issued"].Rows[index]["ClearanceVoucherID"].ToString();
					if (text != "" && text2 != "")
					{
						new FormHelper().EditTransaction(TransactionListType.ChequeClearance, text, text2);
					}
					else
					{
						ErrorHelper.InformationMessage("This Cheque have to be Cleared!.");
					}
				}
			}
			catch (Exception e2)
			{
				ErrorHelper.ProcessError(e2);
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

		public void DuplicateData()
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
			foreach (UltraGridRow row in dataGridItems.Rows)
			{
				foreach (UltraGridCell cell in row.Cells)
				{
					if (cell.Activation == Activation.Disabled)
					{
						cell.Activation = Activation.AllowEdit;
					}
				}
			}
		}

		private void dataGridItems_BeforeEnterEditMode(object sender, CancelEventArgs e)
		{
			checked
			{
				try
				{
					if (dataGridItems.ActiveRow != null)
					{
						UltraGridCell activeCell = dataGridItems.ActiveCell;
						if (activeCell != null)
						{
							CellUIElement cellUIElement = (CellUIElement)activeCell.GetUIElement(dataGridItems.ActiveRowScrollRegion, dataGridItems.ActiveColScrollRegion);
							if (cellUIElement != null)
							{
								int x = cellUIElement.RectInsideBorders.Location.X + dataGridItems.Location.X;
								int y = cellUIElement.RectInsideBorders.Location.Y + dataGridItems.Location.Y;
								int width = cellUIElement.RectInsideBorders.Width;
								int height = cellUIElement.RectInsideBorders.Height;
								if (activeCell.Column.Key == "Chq Date")
								{
									dateTimePickerGrid.SetBounds(x, y, width, height);
									dateTimePickerGrid.Visible = true;
									dateTimePickerGrid.Focus();
									dateTimePickerGrid.BringToFront();
									if (activeCell.Value.ToString() == "" || activeCell.Value == null)
									{
										dateTimePickerGrid.Value = DateTime.Now;
									}
									else
									{
										dateTimePickerGrid.Value = DateTime.Parse(activeCell.Value.ToString());
									}
									isSameRow = true;
									if (e != null)
									{
										e.Cancel = true;
									}
								}
							}
						}
					}
				}
				catch
				{
				}
			}
		}

		private void dataGridItems_SizeChanged(object sender, EventArgs e)
		{
			checked
			{
				if (dataGridItems.ActiveRow != null)
				{
					try
					{
						if (!dateTimePickerGrid.Visible || dataGridItems.ActiveRow == null)
						{
							goto IL_0117;
						}
						UltraGridCell ultraGridCell = dataGridItems.ActiveRow.Cells["Chq Date"];
						if (ultraGridCell != null)
						{
							CellUIElement cellUIElement = (CellUIElement)ultraGridCell.GetUIElement(dataGridItems.ActiveRowScrollRegion, dataGridItems.ActiveColScrollRegion);
							if (cellUIElement != null)
							{
								int x = cellUIElement.RectInsideBorders.Location.X + dataGridItems.Location.X;
								int y = cellUIElement.RectInsideBorders.Location.Y + dataGridItems.Location.Y;
								int width = cellUIElement.RectInsideBorders.Width;
								int height = cellUIElement.RectInsideBorders.Height;
								dateTimePickerGrid.SetBounds(x, y, width, height);
								dateTimePickerGrid.Visible = true;
								goto IL_0117;
							}
						}
						goto end_IL_000f;
						IL_0117:
						if (dateTimePickerGrid.Visible && dataGridItems.ActiveRow != null)
						{
							UltraGridCell ultraGridCell2 = dataGridItems.ActiveRow.Cells["To"];
							if (ultraGridCell2 != null)
							{
								CellUIElement cellUIElement2 = (CellUIElement)ultraGridCell2.GetUIElement(dataGridItems.ActiveRowScrollRegion, dataGridItems.ActiveColScrollRegion);
								if (cellUIElement2 != null)
								{
									int x2 = cellUIElement2.RectInsideBorders.Location.X + dataGridItems.Location.X;
									int y2 = cellUIElement2.RectInsideBorders.Location.Y + dataGridItems.Location.Y;
									int width2 = cellUIElement2.RectInsideBorders.Width;
									int height2 = cellUIElement2.RectInsideBorders.Height;
									dateTimePickerGrid.SetBounds(x2, y2, width2, height2);
								}
							}
						}
						end_IL_000f:;
					}
					catch
					{
					}
				}
			}
		}

		private void dateTimePicker_Leave(object sender, EventArgs e)
		{
			dateTimePickerGrid.Visible = false;
		}

		protected override bool ProcessCmdKey(ref Message msg, Keys keyData)
		{
			if ((keyData == Keys.Tab || keyData == Keys.Return) && base.ActiveControl == dateTimePickerGrid && dataGridItems.ActiveRow != null)
			{
				dataGridItems.ActiveCell = dataGridItems.ActiveRow.Cells["Description"];
				dataGridItems.ActiveRow.Cells["Description"].Activate();
				dateTimePickerGrid.Focus();
				dataGridItems.PerformAction(UltraGridAction.EnterEditMode, shift: false, control: false);
				return true;
			}
			return base.ProcessCmdKey(ref msg, keyData);
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
			Infragistics.Win.Appearance appearance101 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance102 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance103 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance104 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance105 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance106 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance107 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance108 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance109 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance110 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance111 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance112 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance113 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance114 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance115 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance116 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance117 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance118 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance119 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance120 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance121 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance122 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance123 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance124 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance125 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance126 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance127 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance128 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance129 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance130 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance131 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance132 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance133 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance134 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance135 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance136 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance137 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance138 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance139 = new Infragistics.Win.Appearance();
			System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Micromind.ClientUI.WindowsForms.DataEntries.Accounts.ChequePaymentForm));
			panelButtons = new System.Windows.Forms.Panel();
			buttonVoid = new Micromind.UISupport.XPButton();
			buttonDelete = new Micromind.UISupport.XPButton();
			buttonNew = new Micromind.UISupport.XPButton();
			linePanelDown = new Micromind.UISupport.Line();
			xpButton1 = new Micromind.UISupport.XPButton();
			buttonSave = new Micromind.UISupport.XPButton();
			textBoxVoucherNumber = new System.Windows.Forms.TextBox();
			label1 = new System.Windows.Forms.Label();
			textBoxRef1 = new System.Windows.Forms.TextBox();
			textBoxNote = new System.Windows.Forms.TextBox();
			label3 = new System.Windows.Forms.Label();
			labelCurrency = new Infragistics.Win.FormattedLinkLabel.UltraFormattedLinkLabel();
			ultraFormattedLinkLabel2 = new Infragistics.Win.FormattedLinkLabel.UltraFormattedLinkLabel();
			ultraLabel1 = new Infragistics.Win.Misc.UltraLabel();
			ultraGroupBox1 = new Infragistics.Win.Misc.UltraGroupBox();
			labelBalance = new Infragistics.Win.Misc.UltraLabel();
			panelDetails = new System.Windows.Forms.Panel();
			ultraFormattedLinkLabel8 = new Infragistics.Win.FormattedLinkLabel.UltraFormattedLinkLabel();
			buttonSelectInvoice = new Micromind.UISupport.XPButton();
			textBoxAmount = new Micromind.UISupport.AmountTextBox();
			dateTimePickerDeliveredDate = new Micromind.UISupport.MMSDateTimePicker(components);
			label2 = new System.Windows.Forms.Label();
			mmLabel4 = new Micromind.UISupport.MMLabel();
			textBoxTotalDue = new Micromind.UISupport.AmountTextBox();
			label5 = new System.Windows.Forms.Label();
			buttonSelectRequest = new Micromind.UISupport.XPButton();
			textBoxBalance = new System.Windows.Forms.TextBox();
			ultraFormattedLinkLabel1 = new Infragistics.Win.FormattedLinkLabel.UltraFormattedLinkLabel();
			textBoxRequest = new System.Windows.Forms.TextBox();
			dateTimePickerDate = new Micromind.UISupport.flatDatePicker();
			labelAnalysis = new System.Windows.Forms.Label();
			textBoxPayeeName = new System.Windows.Forms.TextBox();
			ultraFormattedLinkLabel5 = new Infragistics.Win.FormattedLinkLabel.UltraFormattedLinkLabel();
			comboBoxSysDoc = new Micromind.DataControls.SysDocComboBox();
			ultraFormattedLinkLabel4 = new Infragistics.Win.FormattedLinkLabel.UltraFormattedLinkLabel();
			comboBoxCostCenter = new Micromind.DataControls.CostCenterComboBox();
			ultraFormattedLinkLabel3 = new Infragistics.Win.FormattedLinkLabel.UltraFormattedLinkLabel();
			payeeSelector1 = new Micromind.DataControls.PayeeSelector();
			currencySelector = new Micromind.DataControls.CurrencySelector();
			mmLabel1 = new Micromind.UISupport.MMLabel();
			comboBoxAnalysis = new Micromind.DataControls.AnalysisComboBox();
			labelVoided = new System.Windows.Forms.Label();
			ultraFormattedLinkLabel6 = new Infragistics.Win.FormattedLinkLabel.UltraFormattedLinkLabel();
			dataGridItems = new Micromind.DataControls.DataEntryGrid();
			formManager = new Micromind.DataControls.FormManager();
			comboBoxChequebook = new Micromind.DataControls.ChequebookComboBox();
			comboBoxConsignExpense = new Micromind.DataControls.ExpenseCodeComboBox();
			comboBoxConsignIn = new Micromind.DataControls.ConsignInComboBox();
			comboBoxCostCategory = new Micromind.DataControls.CostCategoryComboBox();
			comboBoxJob = new Micromind.DataControls.JobComboBox();
			comboBoxProperty = new Micromind.DataControls.PropertyComboBox();
			comboBoxPropertyUnit = new Micromind.DataControls.PropertyUnitComboBox();
			dateTimePickerGrid = new System.Windows.Forms.DateTimePicker();
			panelButtons.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)ultraGroupBox1).BeginInit();
			ultraGroupBox1.SuspendLayout();
			panelDetails.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)comboBoxSysDoc).BeginInit();
			((System.ComponentModel.ISupportInitialize)comboBoxCostCenter).BeginInit();
			((System.ComponentModel.ISupportInitialize)comboBoxAnalysis).BeginInit();
			((System.ComponentModel.ISupportInitialize)dataGridItems).BeginInit();
			((System.ComponentModel.ISupportInitialize)comboBoxChequebook).BeginInit();
			((System.ComponentModel.ISupportInitialize)comboBoxConsignExpense).BeginInit();
			((System.ComponentModel.ISupportInitialize)comboBoxConsignIn).BeginInit();
			((System.ComponentModel.ISupportInitialize)comboBoxCostCategory).BeginInit();
			((System.ComponentModel.ISupportInitialize)comboBoxJob).BeginInit();
			((System.ComponentModel.ISupportInitialize)comboBoxProperty).BeginInit();
			((System.ComponentModel.ISupportInitialize)comboBoxPropertyUnit).BeginInit();
			SuspendLayout();
			panelButtons.Controls.Add(buttonVoid);
			panelButtons.Controls.Add(buttonDelete);
			panelButtons.Controls.Add(buttonNew);
			panelButtons.Controls.Add(linePanelDown);
			panelButtons.Controls.Add(xpButton1);
			panelButtons.Controls.Add(buttonSave);
			panelButtons.Dock = System.Windows.Forms.DockStyle.Bottom;
			panelButtons.Location = new System.Drawing.Point(0, 476);
			panelButtons.Name = "panelButtons";
			panelButtons.Size = new System.Drawing.Size(702, 40);
			panelButtons.TabIndex = 2;
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
			linePanelDown.Size = new System.Drawing.Size(702, 1);
			linePanelDown.TabIndex = 14;
			linePanelDown.TabStop = false;
			xpButton1.AdjustImageLocation = new System.Drawing.Point(0, 0);
			xpButton1.Anchor = (System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right);
			xpButton1.BackColor = System.Drawing.Color.DarkGray;
			xpButton1.BtnShape = Micromind.UISupport.BtnShape.Rectangle;
			xpButton1.BtnStyle = Micromind.UISupport.XPStyle.Default;
			xpButton1.DialogResult = System.Windows.Forms.DialogResult.Cancel;
			xpButton1.ImeMode = System.Windows.Forms.ImeMode.NoControl;
			xpButton1.Location = new System.Drawing.Point(592, 8);
			xpButton1.Name = "xpButton1";
			xpButton1.Size = new System.Drawing.Size(96, 24);
			xpButton1.TabIndex = 4;
			xpButton1.Text = "&Close";
			xpButton1.UseVisualStyleBackColor = false;
			xpButton1.Visible = false;
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
			textBoxVoucherNumber.Location = new System.Drawing.Point(312, 3);
			textBoxVoucherNumber.MaxLength = 15;
			textBoxVoucherNumber.Name = "textBoxVoucherNumber";
			textBoxVoucherNumber.Size = new System.Drawing.Size(123, 20);
			textBoxVoucherNumber.TabIndex = 1;
			label1.AutoSize = true;
			label1.Location = new System.Drawing.Point(227, 97);
			label1.Name = "label1";
			label1.Size = new System.Drawing.Size(60, 13);
			label1.TabIndex = 20;
			label1.Text = "Reference:";
			textBoxRef1.Location = new System.Drawing.Point(302, 94);
			textBoxRef1.MaxLength = 15;
			textBoxRef1.Name = "textBoxRef1";
			textBoxRef1.Size = new System.Drawing.Size(111, 20);
			textBoxRef1.TabIndex = 13;
			textBoxNote.Location = new System.Drawing.Point(90, 118);
			textBoxNote.MaxLength = 255;
			textBoxNote.Multiline = true;
			textBoxNote.Name = "textBoxNote";
			textBoxNote.Size = new System.Drawing.Size(572, 20);
			textBoxNote.TabIndex = 15;
			label3.AutoSize = true;
			label3.Location = new System.Drawing.Point(16, 121);
			label3.Name = "label3";
			label3.Size = new System.Drawing.Size(33, 13);
			label3.TabIndex = 20;
			label3.Text = "Note:";
			appearance.FontData.BoldAsString = "False";
			labelCurrency.Appearance = appearance;
			labelCurrency.AutoSize = true;
			labelCurrency.Location = new System.Drawing.Point(206, 28);
			labelCurrency.Name = "labelCurrency";
			labelCurrency.Size = new System.Drawing.Size(52, 14);
			labelCurrency.TabIndex = 4;
			labelCurrency.TabStop = true;
			labelCurrency.TreatValueAs = Infragistics.Win.FormattedLinkLabel.TreatValueAs.URL;
			labelCurrency.UnderlineLinks = Infragistics.Win.FormattedLinkLabel.UnderlineLink.WhenHovered;
			labelCurrency.Value = "Currency:";
			appearance2.ForeColor = System.Drawing.Color.Blue;
			labelCurrency.VisitedLinkAppearance = appearance2;
			labelCurrency.LinkClicked += new Infragistics.Win.FormattedLinkLabel.LinkClickedEventHandler(ultraFormattedLinkLabel1_LinkClicked);
			appearance3.FontData.BoldAsString = "True";
			appearance3.FontData.Name = "Tahoma";
			ultraFormattedLinkLabel2.Appearance = appearance3;
			ultraFormattedLinkLabel2.AutoSize = true;
			ultraFormattedLinkLabel2.Location = new System.Drawing.Point(206, 5);
			ultraFormattedLinkLabel2.Name = "ultraFormattedLinkLabel2";
			ultraFormattedLinkLabel2.Size = new System.Drawing.Size(101, 15);
			ultraFormattedLinkLabel2.TabIndex = 110;
			ultraFormattedLinkLabel2.TabStop = true;
			ultraFormattedLinkLabel2.TreatValueAs = Infragistics.Win.FormattedLinkLabel.TreatValueAs.URL;
			ultraFormattedLinkLabel2.UnderlineLinks = Infragistics.Win.FormattedLinkLabel.UnderlineLink.WhenHovered;
			ultraFormattedLinkLabel2.Value = "Voucher Number:";
			appearance4.ForeColor = System.Drawing.Color.Blue;
			ultraFormattedLinkLabel2.VisitedLinkAppearance = appearance4;
			ultraFormattedLinkLabel2.LinkClicked += new Infragistics.Win.FormattedLinkLabel.LinkClickedEventHandler(ultraFormattedLinkLabel2_LinkClicked);
			ultraLabel1.Anchor = (System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right);
			appearance5.BorderColor = System.Drawing.Color.FromArgb(122, 150, 223);
			appearance5.FontData.BoldAsString = "True";
			appearance5.FontData.Name = "Tahoma";
			appearance5.TextHAlignAsString = "Right";
			appearance5.TextVAlignAsString = "Middle";
			ultraLabel1.Appearance = appearance5;
			ultraLabel1.BorderStyleInner = Infragistics.Win.UIElementBorderStyle.None;
			ultraLabel1.Location = new System.Drawing.Point(2, 3);
			ultraLabel1.Name = "ultraLabel1";
			ultraLabel1.Size = new System.Drawing.Size(533, 16);
			ultraLabel1.TabIndex = 112;
			ultraLabel1.Text = "Total:";
			ultraGroupBox1.Anchor = (System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right);
			appearance6.BackColor = System.Drawing.Color.FromArgb(194, 216, 252);
			appearance6.BorderColor = System.Drawing.Color.FromArgb(122, 150, 223);
			ultraGroupBox1.Appearance = appearance6;
			ultraGroupBox1.BorderStyle = Infragistics.Win.Misc.GroupBoxBorderStyle.RectangularSolid;
			ultraGroupBox1.Controls.Add(labelBalance);
			ultraGroupBox1.Controls.Add(ultraLabel1);
			ultraGroupBox1.HeaderBorderStyle = Infragistics.Win.UIElementBorderStyle.None;
			ultraGroupBox1.Location = new System.Drawing.Point(11, 441);
			ultraGroupBox1.Name = "ultraGroupBox1";
			ultraGroupBox1.Size = new System.Drawing.Size(678, 21);
			ultraGroupBox1.TabIndex = 17;
			ultraGroupBox1.ViewStyle = Infragistics.Win.Misc.GroupBoxViewStyle.VisualStudio2005;
			labelBalance.Anchor = (System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right);
			appearance7.BorderColor = System.Drawing.Color.FromArgb(122, 150, 223);
			appearance7.FontData.BoldAsString = "True";
			appearance7.FontData.Name = "Tahoma";
			appearance7.TextHAlignAsString = "Right";
			appearance7.TextVAlignAsString = "Middle";
			labelBalance.Appearance = appearance7;
			labelBalance.BorderStyleInner = Infragistics.Win.UIElementBorderStyle.None;
			labelBalance.Location = new System.Drawing.Point(535, 3);
			labelBalance.Name = "labelBalance";
			labelBalance.Size = new System.Drawing.Size(141, 16);
			labelBalance.TabIndex = 113;
			labelBalance.Text = "0.00";
			panelDetails.Controls.Add(ultraFormattedLinkLabel8);
			panelDetails.Controls.Add(buttonSelectInvoice);
			panelDetails.Controls.Add(textBoxAmount);
			panelDetails.Controls.Add(dateTimePickerDeliveredDate);
			panelDetails.Controls.Add(label2);
			panelDetails.Controls.Add(mmLabel4);
			panelDetails.Controls.Add(textBoxTotalDue);
			panelDetails.Controls.Add(label5);
			panelDetails.Controls.Add(buttonSelectRequest);
			panelDetails.Controls.Add(textBoxBalance);
			panelDetails.Controls.Add(ultraFormattedLinkLabel1);
			panelDetails.Controls.Add(textBoxRequest);
			panelDetails.Controls.Add(dateTimePickerDate);
			panelDetails.Controls.Add(labelAnalysis);
			panelDetails.Controls.Add(textBoxPayeeName);
			panelDetails.Controls.Add(ultraFormattedLinkLabel5);
			panelDetails.Controls.Add(comboBoxSysDoc);
			panelDetails.Controls.Add(ultraFormattedLinkLabel4);
			panelDetails.Controls.Add(comboBoxCostCenter);
			panelDetails.Controls.Add(ultraFormattedLinkLabel3);
			panelDetails.Controls.Add(payeeSelector1);
			panelDetails.Controls.Add(ultraFormattedLinkLabel2);
			panelDetails.Controls.Add(labelCurrency);
			panelDetails.Controls.Add(currencySelector);
			panelDetails.Controls.Add(mmLabel1);
			panelDetails.Controls.Add(label3);
			panelDetails.Controls.Add(textBoxNote);
			panelDetails.Controls.Add(label1);
			panelDetails.Controls.Add(textBoxRef1);
			panelDetails.Controls.Add(comboBoxAnalysis);
			panelDetails.Controls.Add(textBoxVoucherNumber);
			panelDetails.Location = new System.Drawing.Point(0, 2);
			panelDetails.Name = "panelDetails";
			panelDetails.Size = new System.Drawing.Size(702, 145);
			panelDetails.TabIndex = 0;
			appearance8.FontData.BoldAsString = "True";
			appearance8.FontData.Name = "Tahoma";
			ultraFormattedLinkLabel8.Appearance = appearance8;
			ultraFormattedLinkLabel8.AutoSize = true;
			ultraFormattedLinkLabel8.Location = new System.Drawing.Point(16, 73);
			ultraFormattedLinkLabel8.Name = "ultraFormattedLinkLabel8";
			ultraFormattedLinkLabel8.Size = new System.Drawing.Size(31, 15);
			ultraFormattedLinkLabel8.TabIndex = 164;
			ultraFormattedLinkLabel8.TabStop = true;
			ultraFormattedLinkLabel8.TreatValueAs = Infragistics.Win.FormattedLinkLabel.TreatValueAs.URL;
			ultraFormattedLinkLabel8.UnderlineLinks = Infragistics.Win.FormattedLinkLabel.UnderlineLink.WhenHovered;
			ultraFormattedLinkLabel8.Value = "Bills:";
			appearance9.ForeColor = System.Drawing.Color.Blue;
			ultraFormattedLinkLabel8.VisitedLinkAppearance = appearance9;
			ultraFormattedLinkLabel8.LinkClicked += new Infragistics.Win.FormattedLinkLabel.LinkClickedEventHandler(ultraFormattedLinkLabel8_LinkClicked);
			buttonSelectInvoice.AdjustImageLocation = new System.Drawing.Point(0, 0);
			buttonSelectInvoice.BackColor = System.Drawing.Color.DarkGray;
			buttonSelectInvoice.BtnShape = Micromind.UISupport.BtnShape.Rectangle;
			buttonSelectInvoice.BtnStyle = Micromind.UISupport.XPStyle.Default;
			buttonSelectInvoice.Enabled = false;
			buttonSelectInvoice.ImeMode = System.Windows.Forms.ImeMode.NoControl;
			buttonSelectInvoice.Location = new System.Drawing.Point(222, 70);
			buttonSelectInvoice.Name = "buttonSelectInvoice";
			buttonSelectInvoice.Size = new System.Drawing.Size(27, 21);
			buttonSelectInvoice.TabIndex = 163;
			buttonSelectInvoice.Text = "...";
			buttonSelectInvoice.UseVisualStyleBackColor = false;
			buttonSelectInvoice.Click += new System.EventHandler(buttonSelectInvoice_Click);
			textBoxAmount.AllowDecimal = true;
			textBoxAmount.BackColor = System.Drawing.Color.WhiteSmoke;
			textBoxAmount.CustomReportFieldName = "";
			textBoxAmount.CustomReportKey = "";
			textBoxAmount.CustomReportValueType = 1;
			textBoxAmount.IsComboTextBox = false;
			textBoxAmount.IsModified = false;
			textBoxAmount.Location = new System.Drawing.Point(90, 71);
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
			textBoxAmount.ReadOnly = true;
			textBoxAmount.Size = new System.Drawing.Size(130, 20);
			textBoxAmount.TabIndex = 9;
			textBoxAmount.Text = "0.00";
			textBoxAmount.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
			textBoxAmount.Value = new decimal(new int[4]
			{
				0,
				0,
				0,
				131072
			});
			dateTimePickerDeliveredDate.Checked = false;
			dateTimePickerDeliveredDate.CustomFormat = " ";
			dateTimePickerDeliveredDate.Format = System.Windows.Forms.DateTimePickerFormat.Short;
			dateTimePickerDeliveredDate.Location = new System.Drawing.Point(508, 94);
			dateTimePickerDeliveredDate.Name = "dateTimePickerDeliveredDate";
			dateTimePickerDeliveredDate.ShowCheckBox = true;
			dateTimePickerDeliveredDate.Size = new System.Drawing.Size(111, 20);
			dateTimePickerDeliveredDate.TabIndex = 14;
			dateTimePickerDeliveredDate.Value = new System.DateTime(0L);
			label2.AutoSize = true;
			label2.Location = new System.Drawing.Point(413, 97);
			label2.Name = "label2";
			label2.Size = new System.Drawing.Size(84, 13);
			label2.TabIndex = 160;
			label2.Text = "Delivered  Date:";
			mmLabel4.AutoSize = true;
			mmLabel4.BorderColor = System.Drawing.Color.FromArgb(78, 122, 171);
			mmLabel4.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25f);
			mmLabel4.IsFieldHeader = false;
			mmLabel4.IsRequired = false;
			mmLabel4.Location = new System.Drawing.Point(414, 73);
			mmLabel4.Name = "mmLabel4";
			mmLabel4.PenWidth = 1f;
			mmLabel4.ShowBorder = false;
			mmLabel4.Size = new System.Drawing.Size(30, 13);
			mmLabel4.TabIndex = 159;
			mmLabel4.Text = "Due:";
			textBoxTotalDue.AllowDecimal = true;
			textBoxTotalDue.BackColor = System.Drawing.Color.WhiteSmoke;
			textBoxTotalDue.CustomReportFieldName = "";
			textBoxTotalDue.CustomReportKey = "";
			textBoxTotalDue.CustomReportValueType = 1;
			textBoxTotalDue.IsComboTextBox = false;
			textBoxTotalDue.IsModified = false;
			textBoxTotalDue.Location = new System.Drawing.Point(458, 71);
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
			textBoxTotalDue.Size = new System.Drawing.Size(95, 20);
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
			label5.AutoSize = true;
			label5.Location = new System.Drawing.Point(258, 74);
			label5.Name = "label5";
			label5.Size = new System.Drawing.Size(49, 13);
			label5.TabIndex = 136;
			label5.Text = "Balance:";
			buttonSelectRequest.AdjustImageLocation = new System.Drawing.Point(0, 0);
			buttonSelectRequest.BackColor = System.Drawing.Color.DarkGray;
			buttonSelectRequest.BtnShape = Micromind.UISupport.BtnShape.Rectangle;
			buttonSelectRequest.BtnStyle = Micromind.UISupport.XPStyle.Default;
			buttonSelectRequest.ImeMode = System.Windows.Forms.ImeMode.NoControl;
			buttonSelectRequest.Location = new System.Drawing.Point(636, 2);
			buttonSelectRequest.Name = "buttonSelectRequest";
			buttonSelectRequest.Size = new System.Drawing.Size(26, 22);
			buttonSelectRequest.TabIndex = 3;
			buttonSelectRequest.Text = "...";
			buttonSelectRequest.UseVisualStyleBackColor = false;
			buttonSelectRequest.Click += new System.EventHandler(buttonSelectRequest_Click);
			textBoxBalance.BackColor = System.Drawing.Color.WhiteSmoke;
			textBoxBalance.Location = new System.Drawing.Point(309, 71);
			textBoxBalance.Name = "textBoxBalance";
			textBoxBalance.ReadOnly = true;
			textBoxBalance.Size = new System.Drawing.Size(105, 20);
			textBoxBalance.TabIndex = 10;
			textBoxBalance.TabStop = false;
			textBoxBalance.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
			appearance10.FontData.BoldAsString = "False";
			appearance10.FontData.Name = "Tahoma";
			ultraFormattedLinkLabel1.Appearance = appearance10;
			ultraFormattedLinkLabel1.AutoSize = true;
			ultraFormattedLinkLabel1.Location = new System.Drawing.Point(441, 5);
			ultraFormattedLinkLabel1.Name = "ultraFormattedLinkLabel1";
			ultraFormattedLinkLabel1.Size = new System.Drawing.Size(48, 15);
			ultraFormattedLinkLabel1.TabIndex = 132;
			ultraFormattedLinkLabel1.TabStop = true;
			ultraFormattedLinkLabel1.TreatValueAs = Infragistics.Win.FormattedLinkLabel.TreatValueAs.URL;
			ultraFormattedLinkLabel1.UnderlineLinks = Infragistics.Win.FormattedLinkLabel.UnderlineLink.WhenHovered;
			ultraFormattedLinkLabel1.Value = "Request:";
			appearance11.ForeColor = System.Drawing.Color.Blue;
			ultraFormattedLinkLabel1.VisitedLinkAppearance = appearance11;
			ultraFormattedLinkLabel1.LinkClicked += new Infragistics.Win.FormattedLinkLabel.LinkClickedEventHandler(ultraFormattedLinkLabel1_LinkClicked_1);
			textBoxRequest.BackColor = System.Drawing.Color.WhiteSmoke;
			textBoxRequest.Location = new System.Drawing.Point(515, 2);
			textBoxRequest.Name = "textBoxRequest";
			textBoxRequest.ReadOnly = true;
			textBoxRequest.Size = new System.Drawing.Size(119, 20);
			textBoxRequest.TabIndex = 2;
			textBoxRequest.TabStop = false;
			dateTimePickerDate.Format = System.Windows.Forms.DateTimePickerFormat.Short;
			dateTimePickerDate.Location = new System.Drawing.Point(90, 25);
			dateTimePickerDate.Name = "dateTimePickerDate";
			dateTimePickerDate.Size = new System.Drawing.Size(111, 20);
			dateTimePickerDate.TabIndex = 4;
			dateTimePickerDate.Value = new System.DateTime(2008, 5, 15, 11, 58, 51, 836);
			labelAnalysis.AutoSize = true;
			labelAnalysis.Location = new System.Drawing.Point(16, 97);
			labelAnalysis.Name = "labelAnalysis";
			labelAnalysis.Size = new System.Drawing.Size(48, 13);
			labelAnalysis.TabIndex = 119;
			labelAnalysis.Text = "Analysis:";
			labelAnalysis.Visible = false;
			textBoxPayeeName.BackColor = System.Drawing.Color.WhiteSmoke;
			textBoxPayeeName.Location = new System.Drawing.Point(369, 47);
			textBoxPayeeName.Name = "textBoxPayeeName";
			textBoxPayeeName.ReadOnly = true;
			textBoxPayeeName.Size = new System.Drawing.Size(293, 20);
			textBoxPayeeName.TabIndex = 8;
			textBoxPayeeName.TabStop = false;
			appearance12.FontData.BoldAsString = "True";
			appearance12.FontData.Name = "Tahoma";
			ultraFormattedLinkLabel5.Appearance = appearance12;
			ultraFormattedLinkLabel5.AutoSize = true;
			ultraFormattedLinkLabel5.Location = new System.Drawing.Point(16, 6);
			ultraFormattedLinkLabel5.Name = "ultraFormattedLinkLabel5";
			ultraFormattedLinkLabel5.Size = new System.Drawing.Size(45, 15);
			ultraFormattedLinkLabel5.TabIndex = 116;
			ultraFormattedLinkLabel5.TabStop = true;
			ultraFormattedLinkLabel5.TreatValueAs = Infragistics.Win.FormattedLinkLabel.TreatValueAs.URL;
			ultraFormattedLinkLabel5.UnderlineLinks = Infragistics.Win.FormattedLinkLabel.UnderlineLink.WhenHovered;
			ultraFormattedLinkLabel5.Value = "Doc ID:";
			appearance13.ForeColor = System.Drawing.Color.Blue;
			ultraFormattedLinkLabel5.VisitedLinkAppearance = appearance13;
			ultraFormattedLinkLabel5.LinkClicked += new Infragistics.Win.FormattedLinkLabel.LinkClickedEventHandler(ultraFormattedLinkLabel5_LinkClicked);
			comboBoxSysDoc.AlwaysInEditMode = true;
			comboBoxSysDoc.Assigned = false;
			comboBoxSysDoc.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper;
			comboBoxSysDoc.CustomReportFieldName = "";
			comboBoxSysDoc.CustomReportKey = "";
			comboBoxSysDoc.CustomReportValueType = 1;
			comboBoxSysDoc.DescriptionTextBox = null;
			appearance14.BackColor = System.Drawing.SystemColors.Window;
			appearance14.BorderColor = System.Drawing.SystemColors.InactiveCaption;
			comboBoxSysDoc.DisplayLayout.Appearance = appearance14;
			comboBoxSysDoc.DisplayLayout.BorderStyle = Infragistics.Win.UIElementBorderStyle.Solid;
			comboBoxSysDoc.DisplayLayout.CaptionVisible = Infragistics.Win.DefaultableBoolean.False;
			appearance15.BackColor = System.Drawing.SystemColors.ActiveBorder;
			appearance15.BackColor2 = System.Drawing.SystemColors.ControlDark;
			appearance15.BackGradientStyle = Infragistics.Win.GradientStyle.Vertical;
			appearance15.BorderColor = System.Drawing.SystemColors.Window;
			comboBoxSysDoc.DisplayLayout.GroupByBox.Appearance = appearance15;
			appearance16.ForeColor = System.Drawing.SystemColors.GrayText;
			comboBoxSysDoc.DisplayLayout.GroupByBox.BandLabelAppearance = appearance16;
			comboBoxSysDoc.DisplayLayout.GroupByBox.BorderStyle = Infragistics.Win.UIElementBorderStyle.Solid;
			appearance17.BackColor = System.Drawing.SystemColors.ControlLightLight;
			appearance17.BackColor2 = System.Drawing.SystemColors.Control;
			appearance17.BackGradientStyle = Infragistics.Win.GradientStyle.Horizontal;
			appearance17.ForeColor = System.Drawing.SystemColors.GrayText;
			comboBoxSysDoc.DisplayLayout.GroupByBox.PromptAppearance = appearance17;
			comboBoxSysDoc.DisplayLayout.MaxColScrollRegions = 1;
			comboBoxSysDoc.DisplayLayout.MaxRowScrollRegions = 1;
			appearance18.BackColor = System.Drawing.SystemColors.Window;
			appearance18.ForeColor = System.Drawing.SystemColors.ControlText;
			comboBoxSysDoc.DisplayLayout.Override.ActiveCellAppearance = appearance18;
			appearance19.BackColor = System.Drawing.SystemColors.Highlight;
			appearance19.ForeColor = System.Drawing.SystemColors.HighlightText;
			comboBoxSysDoc.DisplayLayout.Override.ActiveRowAppearance = appearance19;
			comboBoxSysDoc.DisplayLayout.Override.BorderStyleCell = Infragistics.Win.UIElementBorderStyle.Dotted;
			comboBoxSysDoc.DisplayLayout.Override.BorderStyleRow = Infragistics.Win.UIElementBorderStyle.Dotted;
			appearance20.BackColor = System.Drawing.SystemColors.Window;
			comboBoxSysDoc.DisplayLayout.Override.CardAreaAppearance = appearance20;
			appearance21.BorderColor = System.Drawing.Color.Silver;
			appearance21.TextTrimming = Infragistics.Win.TextTrimming.EllipsisCharacter;
			comboBoxSysDoc.DisplayLayout.Override.CellAppearance = appearance21;
			comboBoxSysDoc.DisplayLayout.Override.CellClickAction = Infragistics.Win.UltraWinGrid.CellClickAction.EditAndSelectText;
			comboBoxSysDoc.DisplayLayout.Override.CellPadding = 0;
			appearance22.BackColor = System.Drawing.SystemColors.Control;
			appearance22.BackColor2 = System.Drawing.SystemColors.ControlDark;
			appearance22.BackGradientAlignment = Infragistics.Win.GradientAlignment.Element;
			appearance22.BackGradientStyle = Infragistics.Win.GradientStyle.Horizontal;
			appearance22.BorderColor = System.Drawing.SystemColors.Window;
			comboBoxSysDoc.DisplayLayout.Override.GroupByRowAppearance = appearance22;
			appearance23.TextHAlignAsString = "Left";
			comboBoxSysDoc.DisplayLayout.Override.HeaderAppearance = appearance23;
			comboBoxSysDoc.DisplayLayout.Override.HeaderClickAction = Infragistics.Win.UltraWinGrid.HeaderClickAction.SortMulti;
			comboBoxSysDoc.DisplayLayout.Override.HeaderStyle = Infragistics.Win.HeaderStyle.WindowsXPCommand;
			appearance24.BackColor = System.Drawing.SystemColors.Window;
			appearance24.BorderColor = System.Drawing.Color.Silver;
			comboBoxSysDoc.DisplayLayout.Override.RowAppearance = appearance24;
			comboBoxSysDoc.DisplayLayout.Override.RowSelectors = Infragistics.Win.DefaultableBoolean.False;
			appearance25.BackColor = System.Drawing.SystemColors.ControlLight;
			comboBoxSysDoc.DisplayLayout.Override.TemplateAddRowAppearance = appearance25;
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
			comboBoxSysDoc.Location = new System.Drawing.Point(90, 3);
			comboBoxSysDoc.MaxDropDownItems = 12;
			comboBoxSysDoc.Name = "comboBoxSysDoc";
			comboBoxSysDoc.ShowAll = false;
			comboBoxSysDoc.ShowInactiveItems = false;
			comboBoxSysDoc.ShowQuickAdd = true;
			comboBoxSysDoc.Size = new System.Drawing.Size(111, 20);
			comboBoxSysDoc.TabIndex = 0;
			comboBoxSysDoc.UseFlatMode = Infragistics.Win.DefaultableBoolean.True;
			appearance26.FontData.BoldAsString = "False";
			appearance26.FontData.Name = "Tahoma";
			ultraFormattedLinkLabel4.Appearance = appearance26;
			ultraFormattedLinkLabel4.AutoSize = true;
			ultraFormattedLinkLabel4.Location = new System.Drawing.Point(441, 27);
			ultraFormattedLinkLabel4.Name = "ultraFormattedLinkLabel4";
			ultraFormattedLinkLabel4.Size = new System.Drawing.Size(65, 15);
			ultraFormattedLinkLabel4.TabIndex = 114;
			ultraFormattedLinkLabel4.TabStop = true;
			ultraFormattedLinkLabel4.TreatValueAs = Infragistics.Win.FormattedLinkLabel.TreatValueAs.URL;
			ultraFormattedLinkLabel4.UnderlineLinks = Infragistics.Win.FormattedLinkLabel.UnderlineLink.WhenHovered;
			ultraFormattedLinkLabel4.Value = "Cost Center:";
			appearance27.ForeColor = System.Drawing.Color.Blue;
			ultraFormattedLinkLabel4.VisitedLinkAppearance = appearance27;
			ultraFormattedLinkLabel4.LinkClicked += new Infragistics.Win.FormattedLinkLabel.LinkClickedEventHandler(ultraFormattedLinkLabel4_LinkClicked);
			comboBoxCostCenter.AlwaysInEditMode = true;
			comboBoxCostCenter.Assigned = false;
			comboBoxCostCenter.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper;
			comboBoxCostCenter.CustomReportFieldName = "";
			comboBoxCostCenter.CustomReportKey = "";
			comboBoxCostCenter.CustomReportValueType = 1;
			comboBoxCostCenter.DescriptionTextBox = null;
			appearance28.BackColor = System.Drawing.SystemColors.Window;
			appearance28.BorderColor = System.Drawing.SystemColors.InactiveCaption;
			comboBoxCostCenter.DisplayLayout.Appearance = appearance28;
			comboBoxCostCenter.DisplayLayout.BorderStyle = Infragistics.Win.UIElementBorderStyle.Solid;
			comboBoxCostCenter.DisplayLayout.CaptionVisible = Infragistics.Win.DefaultableBoolean.False;
			appearance29.BackColor = System.Drawing.SystemColors.ActiveBorder;
			appearance29.BackColor2 = System.Drawing.SystemColors.ControlDark;
			appearance29.BackGradientStyle = Infragistics.Win.GradientStyle.Vertical;
			appearance29.BorderColor = System.Drawing.SystemColors.Window;
			comboBoxCostCenter.DisplayLayout.GroupByBox.Appearance = appearance29;
			appearance30.ForeColor = System.Drawing.SystemColors.GrayText;
			comboBoxCostCenter.DisplayLayout.GroupByBox.BandLabelAppearance = appearance30;
			comboBoxCostCenter.DisplayLayout.GroupByBox.BorderStyle = Infragistics.Win.UIElementBorderStyle.Solid;
			appearance31.BackColor = System.Drawing.SystemColors.ControlLightLight;
			appearance31.BackColor2 = System.Drawing.SystemColors.Control;
			appearance31.BackGradientStyle = Infragistics.Win.GradientStyle.Horizontal;
			appearance31.ForeColor = System.Drawing.SystemColors.GrayText;
			comboBoxCostCenter.DisplayLayout.GroupByBox.PromptAppearance = appearance31;
			comboBoxCostCenter.DisplayLayout.MaxColScrollRegions = 1;
			comboBoxCostCenter.DisplayLayout.MaxRowScrollRegions = 1;
			appearance32.BackColor = System.Drawing.SystemColors.Window;
			appearance32.ForeColor = System.Drawing.SystemColors.ControlText;
			comboBoxCostCenter.DisplayLayout.Override.ActiveCellAppearance = appearance32;
			appearance33.BackColor = System.Drawing.SystemColors.Highlight;
			appearance33.ForeColor = System.Drawing.SystemColors.HighlightText;
			comboBoxCostCenter.DisplayLayout.Override.ActiveRowAppearance = appearance33;
			comboBoxCostCenter.DisplayLayout.Override.BorderStyleCell = Infragistics.Win.UIElementBorderStyle.Dotted;
			comboBoxCostCenter.DisplayLayout.Override.BorderStyleRow = Infragistics.Win.UIElementBorderStyle.Dotted;
			appearance34.BackColor = System.Drawing.SystemColors.Window;
			comboBoxCostCenter.DisplayLayout.Override.CardAreaAppearance = appearance34;
			appearance35.BorderColor = System.Drawing.Color.Silver;
			appearance35.TextTrimming = Infragistics.Win.TextTrimming.EllipsisCharacter;
			comboBoxCostCenter.DisplayLayout.Override.CellAppearance = appearance35;
			comboBoxCostCenter.DisplayLayout.Override.CellClickAction = Infragistics.Win.UltraWinGrid.CellClickAction.EditAndSelectText;
			comboBoxCostCenter.DisplayLayout.Override.CellPadding = 0;
			appearance36.BackColor = System.Drawing.SystemColors.Control;
			appearance36.BackColor2 = System.Drawing.SystemColors.ControlDark;
			appearance36.BackGradientAlignment = Infragistics.Win.GradientAlignment.Element;
			appearance36.BackGradientStyle = Infragistics.Win.GradientStyle.Horizontal;
			appearance36.BorderColor = System.Drawing.SystemColors.Window;
			comboBoxCostCenter.DisplayLayout.Override.GroupByRowAppearance = appearance36;
			appearance37.TextHAlignAsString = "Left";
			comboBoxCostCenter.DisplayLayout.Override.HeaderAppearance = appearance37;
			comboBoxCostCenter.DisplayLayout.Override.HeaderClickAction = Infragistics.Win.UltraWinGrid.HeaderClickAction.SortMulti;
			comboBoxCostCenter.DisplayLayout.Override.HeaderStyle = Infragistics.Win.HeaderStyle.WindowsXPCommand;
			appearance38.BackColor = System.Drawing.SystemColors.Window;
			appearance38.BorderColor = System.Drawing.Color.Silver;
			comboBoxCostCenter.DisplayLayout.Override.RowAppearance = appearance38;
			comboBoxCostCenter.DisplayLayout.Override.RowSelectors = Infragistics.Win.DefaultableBoolean.False;
			appearance39.BackColor = System.Drawing.SystemColors.ControlLight;
			comboBoxCostCenter.DisplayLayout.Override.TemplateAddRowAppearance = appearance39;
			comboBoxCostCenter.DisplayLayout.ScrollBounds = Infragistics.Win.UltraWinGrid.ScrollBounds.ScrollToFill;
			comboBoxCostCenter.DisplayLayout.ScrollStyle = Infragistics.Win.UltraWinGrid.ScrollStyle.Immediate;
			comboBoxCostCenter.DisplayLayout.ViewStyleBand = Infragistics.Win.UltraWinGrid.ViewStyleBand.OutlookGroupBy;
			comboBoxCostCenter.DropDownSearchMethod = Infragistics.Win.UltraWinGrid.DropDownSearchMethod.Linear;
			comboBoxCostCenter.Editable = true;
			comboBoxCostCenter.FilterString = "";
			comboBoxCostCenter.HasAllAccount = false;
			comboBoxCostCenter.HasCustom = false;
			comboBoxCostCenter.IsDataLoaded = false;
			comboBoxCostCenter.Location = new System.Drawing.Point(515, 24);
			comboBoxCostCenter.MaxDropDownItems = 12;
			comboBoxCostCenter.Name = "comboBoxCostCenter";
			comboBoxCostCenter.ShowInactiveItems = false;
			comboBoxCostCenter.ShowQuickAdd = true;
			comboBoxCostCenter.Size = new System.Drawing.Size(147, 20);
			comboBoxCostCenter.TabIndex = 6;
			comboBoxCostCenter.UseFlatMode = Infragistics.Win.DefaultableBoolean.True;
			appearance40.FontData.BoldAsString = "True";
			appearance40.FontData.Name = "Tahoma";
			ultraFormattedLinkLabel3.Appearance = appearance40;
			ultraFormattedLinkLabel3.AutoSize = true;
			ultraFormattedLinkLabel3.Location = new System.Drawing.Point(16, 49);
			ultraFormattedLinkLabel3.Name = "ultraFormattedLinkLabel3";
			ultraFormattedLinkLabel3.Size = new System.Drawing.Size(49, 15);
			ultraFormattedLinkLabel3.TabIndex = 112;
			ultraFormattedLinkLabel3.TabStop = true;
			ultraFormattedLinkLabel3.TreatValueAs = Infragistics.Win.FormattedLinkLabel.TreatValueAs.URL;
			ultraFormattedLinkLabel3.UnderlineLinks = Infragistics.Win.FormattedLinkLabel.UnderlineLink.WhenHovered;
			ultraFormattedLinkLabel3.Value = "Paid To:";
			appearance41.ForeColor = System.Drawing.Color.Blue;
			ultraFormattedLinkLabel3.VisitedLinkAppearance = appearance41;
			ultraFormattedLinkLabel3.LinkClicked += new Infragistics.Win.FormattedLinkLabel.LinkClickedEventHandler(ultraFormattedLinkLabel3_LinkClicked);
			payeeSelector1.BackColor = System.Drawing.Color.Transparent;
			payeeSelector1.Location = new System.Drawing.Point(90, 47);
			payeeSelector1.MaximumSize = new System.Drawing.Size(2000, 20);
			payeeSelector1.MinimumSize = new System.Drawing.Size(0, 20);
			payeeSelector1.Name = "payeeSelector1";
			payeeSelector1.SelectedID = "";
			payeeSelector1.SelectedType = "";
			payeeSelector1.Size = new System.Drawing.Size(273, 20);
			payeeSelector1.TabIndex = 7;
			currencySelector.BackColor = System.Drawing.Color.WhiteSmoke;
			currencySelector.Location = new System.Drawing.Point(263, 25);
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
			currencySelector.Size = new System.Drawing.Size(172, 20);
			currencySelector.TabIndex = 5;
			mmLabel1.AutoSize = true;
			mmLabel1.BorderColor = System.Drawing.Color.FromArgb(78, 122, 171);
			mmLabel1.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25f, System.Drawing.FontStyle.Bold);
			mmLabel1.IsFieldHeader = false;
			mmLabel1.IsRequired = true;
			mmLabel1.Location = new System.Drawing.Point(16, 28);
			mmLabel1.Name = "mmLabel1";
			mmLabel1.PenWidth = 1f;
			mmLabel1.ShowBorder = false;
			mmLabel1.Size = new System.Drawing.Size(38, 13);
			mmLabel1.TabIndex = 2;
			mmLabel1.Text = "Date:";
			comboBoxAnalysis.AlwaysInEditMode = true;
			comboBoxAnalysis.Assigned = false;
			comboBoxAnalysis.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper;
			comboBoxAnalysis.CustomReportFieldName = "";
			comboBoxAnalysis.CustomReportKey = "";
			comboBoxAnalysis.CustomReportValueType = 1;
			comboBoxAnalysis.DescriptionTextBox = null;
			appearance42.BackColor = System.Drawing.SystemColors.Window;
			appearance42.BorderColor = System.Drawing.SystemColors.InactiveCaption;
			comboBoxAnalysis.DisplayLayout.Appearance = appearance42;
			comboBoxAnalysis.DisplayLayout.BorderStyle = Infragistics.Win.UIElementBorderStyle.Solid;
			comboBoxAnalysis.DisplayLayout.CaptionVisible = Infragistics.Win.DefaultableBoolean.False;
			appearance43.BackColor = System.Drawing.SystemColors.ActiveBorder;
			appearance43.BackColor2 = System.Drawing.SystemColors.ControlDark;
			appearance43.BackGradientStyle = Infragistics.Win.GradientStyle.Vertical;
			appearance43.BorderColor = System.Drawing.SystemColors.Window;
			comboBoxAnalysis.DisplayLayout.GroupByBox.Appearance = appearance43;
			appearance44.ForeColor = System.Drawing.SystemColors.GrayText;
			comboBoxAnalysis.DisplayLayout.GroupByBox.BandLabelAppearance = appearance44;
			comboBoxAnalysis.DisplayLayout.GroupByBox.BorderStyle = Infragistics.Win.UIElementBorderStyle.Solid;
			appearance45.BackColor = System.Drawing.SystemColors.ControlLightLight;
			appearance45.BackColor2 = System.Drawing.SystemColors.Control;
			appearance45.BackGradientStyle = Infragistics.Win.GradientStyle.Horizontal;
			appearance45.ForeColor = System.Drawing.SystemColors.GrayText;
			comboBoxAnalysis.DisplayLayout.GroupByBox.PromptAppearance = appearance45;
			comboBoxAnalysis.DisplayLayout.MaxColScrollRegions = 1;
			comboBoxAnalysis.DisplayLayout.MaxRowScrollRegions = 1;
			appearance46.BackColor = System.Drawing.SystemColors.Window;
			appearance46.ForeColor = System.Drawing.SystemColors.ControlText;
			comboBoxAnalysis.DisplayLayout.Override.ActiveCellAppearance = appearance46;
			appearance47.BackColor = System.Drawing.SystemColors.Highlight;
			appearance47.ForeColor = System.Drawing.SystemColors.HighlightText;
			comboBoxAnalysis.DisplayLayout.Override.ActiveRowAppearance = appearance47;
			comboBoxAnalysis.DisplayLayout.Override.BorderStyleCell = Infragistics.Win.UIElementBorderStyle.Dotted;
			comboBoxAnalysis.DisplayLayout.Override.BorderStyleRow = Infragistics.Win.UIElementBorderStyle.Dotted;
			appearance48.BackColor = System.Drawing.SystemColors.Window;
			comboBoxAnalysis.DisplayLayout.Override.CardAreaAppearance = appearance48;
			appearance49.BorderColor = System.Drawing.Color.Silver;
			appearance49.TextTrimming = Infragistics.Win.TextTrimming.EllipsisCharacter;
			comboBoxAnalysis.DisplayLayout.Override.CellAppearance = appearance49;
			comboBoxAnalysis.DisplayLayout.Override.CellClickAction = Infragistics.Win.UltraWinGrid.CellClickAction.EditAndSelectText;
			comboBoxAnalysis.DisplayLayout.Override.CellPadding = 0;
			appearance50.BackColor = System.Drawing.SystemColors.Control;
			appearance50.BackColor2 = System.Drawing.SystemColors.ControlDark;
			appearance50.BackGradientAlignment = Infragistics.Win.GradientAlignment.Element;
			appearance50.BackGradientStyle = Infragistics.Win.GradientStyle.Horizontal;
			appearance50.BorderColor = System.Drawing.SystemColors.Window;
			comboBoxAnalysis.DisplayLayout.Override.GroupByRowAppearance = appearance50;
			appearance51.TextHAlignAsString = "Left";
			comboBoxAnalysis.DisplayLayout.Override.HeaderAppearance = appearance51;
			comboBoxAnalysis.DisplayLayout.Override.HeaderClickAction = Infragistics.Win.UltraWinGrid.HeaderClickAction.SortMulti;
			comboBoxAnalysis.DisplayLayout.Override.HeaderStyle = Infragistics.Win.HeaderStyle.WindowsXPCommand;
			appearance52.BackColor = System.Drawing.SystemColors.Window;
			appearance52.BorderColor = System.Drawing.Color.Silver;
			comboBoxAnalysis.DisplayLayout.Override.RowAppearance = appearance52;
			comboBoxAnalysis.DisplayLayout.Override.RowSelectors = Infragistics.Win.DefaultableBoolean.False;
			appearance53.BackColor = System.Drawing.SystemColors.ControlLight;
			comboBoxAnalysis.DisplayLayout.Override.TemplateAddRowAppearance = appearance53;
			comboBoxAnalysis.DisplayLayout.ScrollBounds = Infragistics.Win.UltraWinGrid.ScrollBounds.ScrollToFill;
			comboBoxAnalysis.DisplayLayout.ScrollStyle = Infragistics.Win.UltraWinGrid.ScrollStyle.Immediate;
			comboBoxAnalysis.DisplayLayout.ViewStyleBand = Infragistics.Win.UltraWinGrid.ViewStyleBand.OutlookGroupBy;
			comboBoxAnalysis.DropDownSearchMethod = Infragistics.Win.UltraWinGrid.DropDownSearchMethod.Linear;
			comboBoxAnalysis.Editable = true;
			comboBoxAnalysis.FilterString = "";
			comboBoxAnalysis.HasAllAccount = false;
			comboBoxAnalysis.HasCustom = false;
			comboBoxAnalysis.IsDataLoaded = false;
			comboBoxAnalysis.Location = new System.Drawing.Point(90, 94);
			comboBoxAnalysis.MaxDropDownItems = 12;
			comboBoxAnalysis.Name = "comboBoxAnalysis";
			comboBoxAnalysis.ShowInactiveItems = false;
			comboBoxAnalysis.ShowQuickAdd = true;
			comboBoxAnalysis.Size = new System.Drawing.Size(130, 20);
			comboBoxAnalysis.TabIndex = 12;
			comboBoxAnalysis.UseFlatMode = Infragistics.Win.DefaultableBoolean.True;
			comboBoxAnalysis.Visible = false;
			labelVoided.Anchor = (System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right);
			labelVoided.BackColor = System.Drawing.Color.White;
			labelVoided.Font = new System.Drawing.Font("Microsoft Sans Serif", 14f, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0);
			labelVoided.ForeColor = System.Drawing.Color.DarkRed;
			labelVoided.Location = new System.Drawing.Point(14, 358);
			labelVoided.Name = "labelVoided";
			labelVoided.Size = new System.Drawing.Size(675, 55);
			labelVoided.TabIndex = 117;
			labelVoided.Text = "VOIDED";
			labelVoided.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
			labelVoided.Visible = false;
			ultraFormattedLinkLabel6.Anchor = (System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left);
			appearance54.FontData.BoldAsString = "False";
			appearance54.FontData.Name = "Tahoma";
			ultraFormattedLinkLabel6.Appearance = appearance54;
			ultraFormattedLinkLabel6.AutoSize = true;
			ultraFormattedLinkLabel6.Location = new System.Drawing.Point(12, 461);
			ultraFormattedLinkLabel6.Name = "ultraFormattedLinkLabel6";
			ultraFormattedLinkLabel6.Size = new System.Drawing.Size(88, 15);
			ultraFormattedLinkLabel6.TabIndex = 135;
			ultraFormattedLinkLabel6.TabStop = true;
			ultraFormattedLinkLabel6.TreatValueAs = Infragistics.Win.FormattedLinkLabel.TreatValueAs.URL;
			ultraFormattedLinkLabel6.UnderlineLinks = Infragistics.Win.FormattedLinkLabel.UnderlineLink.WhenHovered;
			ultraFormattedLinkLabel6.Value = "Clearance Details";
			appearance55.ForeColor = System.Drawing.Color.Blue;
			ultraFormattedLinkLabel6.VisitedLinkAppearance = appearance55;
			ultraFormattedLinkLabel6.LinkClicked += new Infragistics.Win.FormattedLinkLabel.LinkClickedEventHandler(ultraFormattedLinkLabel6_LinkClicked);
			dataGridItems.AllowAddNew = false;
			dataGridItems.Anchor = (System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right);
			appearance56.BackColor = System.Drawing.SystemColors.Window;
			appearance56.BorderColor = System.Drawing.SystemColors.InactiveCaption;
			dataGridItems.DisplayLayout.Appearance = appearance56;
			dataGridItems.DisplayLayout.BorderStyle = Infragistics.Win.UIElementBorderStyle.Solid;
			dataGridItems.DisplayLayout.CaptionVisible = Infragistics.Win.DefaultableBoolean.False;
			appearance57.BackColor = System.Drawing.SystemColors.ActiveBorder;
			appearance57.BackColor2 = System.Drawing.SystemColors.ControlDark;
			appearance57.BackGradientStyle = Infragistics.Win.GradientStyle.Vertical;
			appearance57.BorderColor = System.Drawing.SystemColors.Window;
			dataGridItems.DisplayLayout.GroupByBox.Appearance = appearance57;
			appearance58.ForeColor = System.Drawing.SystemColors.GrayText;
			dataGridItems.DisplayLayout.GroupByBox.BandLabelAppearance = appearance58;
			dataGridItems.DisplayLayout.GroupByBox.BorderStyle = Infragistics.Win.UIElementBorderStyle.Solid;
			appearance59.BackColor = System.Drawing.SystemColors.ControlLightLight;
			appearance59.BackColor2 = System.Drawing.SystemColors.Control;
			appearance59.BackGradientStyle = Infragistics.Win.GradientStyle.Horizontal;
			appearance59.ForeColor = System.Drawing.SystemColors.GrayText;
			dataGridItems.DisplayLayout.GroupByBox.PromptAppearance = appearance59;
			dataGridItems.DisplayLayout.MaxColScrollRegions = 1;
			dataGridItems.DisplayLayout.MaxRowScrollRegions = 1;
			appearance60.BackColor = System.Drawing.SystemColors.Window;
			appearance60.ForeColor = System.Drawing.SystemColors.ControlText;
			dataGridItems.DisplayLayout.Override.ActiveCellAppearance = appearance60;
			appearance61.BackColor = System.Drawing.SystemColors.Highlight;
			appearance61.ForeColor = System.Drawing.SystemColors.HighlightText;
			dataGridItems.DisplayLayout.Override.ActiveRowAppearance = appearance61;
			dataGridItems.DisplayLayout.Override.AllowAddNew = Infragistics.Win.UltraWinGrid.AllowAddNew.No;
			dataGridItems.DisplayLayout.Override.BorderStyleCell = Infragistics.Win.UIElementBorderStyle.Dotted;
			dataGridItems.DisplayLayout.Override.BorderStyleRow = Infragistics.Win.UIElementBorderStyle.Dotted;
			appearance62.BackColor = System.Drawing.SystemColors.Window;
			dataGridItems.DisplayLayout.Override.CardAreaAppearance = appearance62;
			appearance63.BorderColor = System.Drawing.Color.Silver;
			appearance63.TextTrimming = Infragistics.Win.TextTrimming.EllipsisCharacter;
			dataGridItems.DisplayLayout.Override.CellAppearance = appearance63;
			dataGridItems.DisplayLayout.Override.CellClickAction = Infragistics.Win.UltraWinGrid.CellClickAction.EditAndSelectText;
			dataGridItems.DisplayLayout.Override.CellPadding = 0;
			appearance64.BackColor = System.Drawing.SystemColors.Control;
			appearance64.BackColor2 = System.Drawing.SystemColors.ControlDark;
			appearance64.BackGradientAlignment = Infragistics.Win.GradientAlignment.Element;
			appearance64.BackGradientStyle = Infragistics.Win.GradientStyle.Horizontal;
			appearance64.BorderColor = System.Drawing.SystemColors.Window;
			dataGridItems.DisplayLayout.Override.GroupByRowAppearance = appearance64;
			appearance65.TextHAlignAsString = "Left";
			dataGridItems.DisplayLayout.Override.HeaderAppearance = appearance65;
			dataGridItems.DisplayLayout.Override.HeaderClickAction = Infragistics.Win.UltraWinGrid.HeaderClickAction.SortMulti;
			dataGridItems.DisplayLayout.Override.HeaderStyle = Infragistics.Win.HeaderStyle.WindowsXPCommand;
			appearance66.BackColor = System.Drawing.SystemColors.Window;
			appearance66.BorderColor = System.Drawing.Color.Silver;
			dataGridItems.DisplayLayout.Override.RowAppearance = appearance66;
			dataGridItems.DisplayLayout.Override.RowSelectors = Infragistics.Win.DefaultableBoolean.False;
			appearance67.BackColor = System.Drawing.SystemColors.ControlLight;
			dataGridItems.DisplayLayout.Override.TemplateAddRowAppearance = appearance67;
			dataGridItems.DisplayLayout.ScrollBounds = Infragistics.Win.UltraWinGrid.ScrollBounds.ScrollToFill;
			dataGridItems.DisplayLayout.ScrollStyle = Infragistics.Win.UltraWinGrid.ScrollStyle.Immediate;
			dataGridItems.DisplayLayout.TabNavigation = Infragistics.Win.UltraWinGrid.TabNavigation.NextControlOnLastCell;
			dataGridItems.DisplayLayout.ViewStyleBand = Infragistics.Win.UltraWinGrid.ViewStyleBand.OutlookGroupBy;
			dataGridItems.ExitEditModeOnLeave = false;
			dataGridItems.IncludeLotItems = false;
			dataGridItems.LoadLayoutFailed = false;
			dataGridItems.Location = new System.Drawing.Point(12, 153);
			dataGridItems.MinimumSize = new System.Drawing.Size(622, 154);
			dataGridItems.Name = "dataGridItems";
			dataGridItems.ShowClearMenu = true;
			dataGridItems.ShowDeleteMenu = true;
			dataGridItems.ShowInsertMenu = true;
			dataGridItems.ShowMoveRowsMenu = true;
			dataGridItems.Size = new System.Drawing.Size(677, 290);
			dataGridItems.TabIndex = 1;
			dataGridItems.Text = "dataEntryGrid1";
			dataGridItems.AfterCellActivate += new System.EventHandler(dataGridItems_AfterCellActivate);
			formManager.BackColor = System.Drawing.Color.RosyBrown;
			formManager.Dock = System.Windows.Forms.DockStyle.Left;
			formManager.IsForcedDirty = false;
			formManager.Location = new System.Drawing.Point(0, 0);
			formManager.MaximumSize = new System.Drawing.Size(20, 20);
			formManager.MinimumSize = new System.Drawing.Size(20, 20);
			formManager.Name = "formManager";
			formManager.Size = new System.Drawing.Size(20, 20);
			formManager.TabIndex = 16;
			formManager.Text = "formManager1";
			formManager.Visible = false;
			comboBoxChequebook.AlwaysInEditMode = true;
			comboBoxChequebook.Assigned = false;
			comboBoxChequebook.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper;
			comboBoxChequebook.CustomReportFieldName = "";
			comboBoxChequebook.CustomReportKey = "";
			comboBoxChequebook.CustomReportValueType = 1;
			comboBoxChequebook.DescriptionTextBox = null;
			appearance68.BackColor = System.Drawing.SystemColors.Window;
			appearance68.BorderColor = System.Drawing.SystemColors.InactiveCaption;
			comboBoxChequebook.DisplayLayout.Appearance = appearance68;
			comboBoxChequebook.DisplayLayout.BorderStyle = Infragistics.Win.UIElementBorderStyle.Solid;
			comboBoxChequebook.DisplayLayout.CaptionVisible = Infragistics.Win.DefaultableBoolean.False;
			appearance69.BackColor = System.Drawing.SystemColors.ActiveBorder;
			appearance69.BackColor2 = System.Drawing.SystemColors.ControlDark;
			appearance69.BackGradientStyle = Infragistics.Win.GradientStyle.Vertical;
			appearance69.BorderColor = System.Drawing.SystemColors.Window;
			comboBoxChequebook.DisplayLayout.GroupByBox.Appearance = appearance69;
			appearance70.ForeColor = System.Drawing.SystemColors.GrayText;
			comboBoxChequebook.DisplayLayout.GroupByBox.BandLabelAppearance = appearance70;
			comboBoxChequebook.DisplayLayout.GroupByBox.BorderStyle = Infragistics.Win.UIElementBorderStyle.Solid;
			appearance71.BackColor = System.Drawing.SystemColors.ControlLightLight;
			appearance71.BackColor2 = System.Drawing.SystemColors.Control;
			appearance71.BackGradientStyle = Infragistics.Win.GradientStyle.Horizontal;
			appearance71.ForeColor = System.Drawing.SystemColors.GrayText;
			comboBoxChequebook.DisplayLayout.GroupByBox.PromptAppearance = appearance71;
			comboBoxChequebook.DisplayLayout.MaxColScrollRegions = 1;
			comboBoxChequebook.DisplayLayout.MaxRowScrollRegions = 1;
			appearance72.BackColor = System.Drawing.SystemColors.Window;
			appearance72.ForeColor = System.Drawing.SystemColors.ControlText;
			comboBoxChequebook.DisplayLayout.Override.ActiveCellAppearance = appearance72;
			appearance73.BackColor = System.Drawing.SystemColors.Highlight;
			appearance73.ForeColor = System.Drawing.SystemColors.HighlightText;
			comboBoxChequebook.DisplayLayout.Override.ActiveRowAppearance = appearance73;
			comboBoxChequebook.DisplayLayout.Override.BorderStyleCell = Infragistics.Win.UIElementBorderStyle.Dotted;
			comboBoxChequebook.DisplayLayout.Override.BorderStyleRow = Infragistics.Win.UIElementBorderStyle.Dotted;
			appearance74.BackColor = System.Drawing.SystemColors.Window;
			comboBoxChequebook.DisplayLayout.Override.CardAreaAppearance = appearance74;
			appearance75.BorderColor = System.Drawing.Color.Silver;
			appearance75.TextTrimming = Infragistics.Win.TextTrimming.EllipsisCharacter;
			comboBoxChequebook.DisplayLayout.Override.CellAppearance = appearance75;
			comboBoxChequebook.DisplayLayout.Override.CellClickAction = Infragistics.Win.UltraWinGrid.CellClickAction.EditAndSelectText;
			comboBoxChequebook.DisplayLayout.Override.CellPadding = 0;
			appearance76.BackColor = System.Drawing.SystemColors.Control;
			appearance76.BackColor2 = System.Drawing.SystemColors.ControlDark;
			appearance76.BackGradientAlignment = Infragistics.Win.GradientAlignment.Element;
			appearance76.BackGradientStyle = Infragistics.Win.GradientStyle.Horizontal;
			appearance76.BorderColor = System.Drawing.SystemColors.Window;
			comboBoxChequebook.DisplayLayout.Override.GroupByRowAppearance = appearance76;
			appearance77.TextHAlignAsString = "Left";
			comboBoxChequebook.DisplayLayout.Override.HeaderAppearance = appearance77;
			comboBoxChequebook.DisplayLayout.Override.HeaderClickAction = Infragistics.Win.UltraWinGrid.HeaderClickAction.SortMulti;
			comboBoxChequebook.DisplayLayout.Override.HeaderStyle = Infragistics.Win.HeaderStyle.WindowsXPCommand;
			appearance78.BackColor = System.Drawing.SystemColors.Window;
			appearance78.BorderColor = System.Drawing.Color.Silver;
			comboBoxChequebook.DisplayLayout.Override.RowAppearance = appearance78;
			comboBoxChequebook.DisplayLayout.Override.RowSelectors = Infragistics.Win.DefaultableBoolean.False;
			appearance79.BackColor = System.Drawing.SystemColors.ControlLight;
			comboBoxChequebook.DisplayLayout.Override.TemplateAddRowAppearance = appearance79;
			comboBoxChequebook.DisplayLayout.ScrollBounds = Infragistics.Win.UltraWinGrid.ScrollBounds.ScrollToFill;
			comboBoxChequebook.DisplayLayout.ScrollStyle = Infragistics.Win.UltraWinGrid.ScrollStyle.Immediate;
			comboBoxChequebook.DisplayLayout.ViewStyleBand = Infragistics.Win.UltraWinGrid.ViewStyleBand.OutlookGroupBy;
			comboBoxChequebook.DropDownSearchMethod = Infragistics.Win.UltraWinGrid.DropDownSearchMethod.Linear;
			comboBoxChequebook.Editable = true;
			comboBoxChequebook.FilterString = "";
			comboBoxChequebook.HasAllAccount = false;
			comboBoxChequebook.HasCustom = false;
			comboBoxChequebook.IsDataLoaded = false;
			comboBoxChequebook.Location = new System.Drawing.Point(400, 220);
			comboBoxChequebook.MaxDropDownItems = 12;
			comboBoxChequebook.Name = "comboBoxChequebook";
			comboBoxChequebook.ShowInactiveItems = false;
			comboBoxChequebook.ShowQuickAdd = true;
			comboBoxChequebook.Size = new System.Drawing.Size(46, 20);
			comboBoxChequebook.TabIndex = 122;
			comboBoxChequebook.UseFlatMode = Infragistics.Win.DefaultableBoolean.True;
			comboBoxChequebook.Visible = false;
			comboBoxConsignExpense.Assigned = false;
			comboBoxConsignExpense.AutoCompleteMode = Infragistics.Win.AutoCompleteMode.Append;
			comboBoxConsignExpense.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper;
			comboBoxConsignExpense.CustomReportFieldName = "";
			comboBoxConsignExpense.CustomReportKey = "";
			comboBoxConsignExpense.CustomReportValueType = 1;
			comboBoxConsignExpense.DescriptionTextBox = null;
			appearance80.BackColor = System.Drawing.SystemColors.Window;
			appearance80.BorderColor = System.Drawing.SystemColors.InactiveCaption;
			comboBoxConsignExpense.DisplayLayout.Appearance = appearance80;
			comboBoxConsignExpense.DisplayLayout.BorderStyle = Infragistics.Win.UIElementBorderStyle.Solid;
			comboBoxConsignExpense.DisplayLayout.CaptionVisible = Infragistics.Win.DefaultableBoolean.False;
			appearance81.BackColor = System.Drawing.SystemColors.ActiveBorder;
			appearance81.BackColor2 = System.Drawing.SystemColors.ControlDark;
			appearance81.BackGradientStyle = Infragistics.Win.GradientStyle.Vertical;
			appearance81.BorderColor = System.Drawing.SystemColors.Window;
			comboBoxConsignExpense.DisplayLayout.GroupByBox.Appearance = appearance81;
			appearance82.ForeColor = System.Drawing.SystemColors.GrayText;
			comboBoxConsignExpense.DisplayLayout.GroupByBox.BandLabelAppearance = appearance82;
			comboBoxConsignExpense.DisplayLayout.GroupByBox.BorderStyle = Infragistics.Win.UIElementBorderStyle.Solid;
			appearance83.BackColor = System.Drawing.SystemColors.ControlLightLight;
			appearance83.BackColor2 = System.Drawing.SystemColors.Control;
			appearance83.BackGradientStyle = Infragistics.Win.GradientStyle.Horizontal;
			appearance83.ForeColor = System.Drawing.SystemColors.GrayText;
			comboBoxConsignExpense.DisplayLayout.GroupByBox.PromptAppearance = appearance83;
			comboBoxConsignExpense.DisplayLayout.MaxColScrollRegions = 1;
			comboBoxConsignExpense.DisplayLayout.MaxRowScrollRegions = 1;
			appearance84.BackColor = System.Drawing.SystemColors.Window;
			appearance84.ForeColor = System.Drawing.SystemColors.ControlText;
			comboBoxConsignExpense.DisplayLayout.Override.ActiveCellAppearance = appearance84;
			appearance85.BackColor = System.Drawing.SystemColors.Highlight;
			appearance85.ForeColor = System.Drawing.SystemColors.HighlightText;
			comboBoxConsignExpense.DisplayLayout.Override.ActiveRowAppearance = appearance85;
			comboBoxConsignExpense.DisplayLayout.Override.BorderStyleCell = Infragistics.Win.UIElementBorderStyle.Dotted;
			comboBoxConsignExpense.DisplayLayout.Override.BorderStyleRow = Infragistics.Win.UIElementBorderStyle.Dotted;
			appearance86.BackColor = System.Drawing.SystemColors.Window;
			comboBoxConsignExpense.DisplayLayout.Override.CardAreaAppearance = appearance86;
			appearance87.BorderColor = System.Drawing.Color.Silver;
			appearance87.TextTrimming = Infragistics.Win.TextTrimming.EllipsisCharacter;
			comboBoxConsignExpense.DisplayLayout.Override.CellAppearance = appearance87;
			comboBoxConsignExpense.DisplayLayout.Override.CellClickAction = Infragistics.Win.UltraWinGrid.CellClickAction.EditAndSelectText;
			comboBoxConsignExpense.DisplayLayout.Override.CellPadding = 0;
			appearance88.BackColor = System.Drawing.SystemColors.Control;
			appearance88.BackColor2 = System.Drawing.SystemColors.ControlDark;
			appearance88.BackGradientAlignment = Infragistics.Win.GradientAlignment.Element;
			appearance88.BackGradientStyle = Infragistics.Win.GradientStyle.Horizontal;
			appearance88.BorderColor = System.Drawing.SystemColors.Window;
			comboBoxConsignExpense.DisplayLayout.Override.GroupByRowAppearance = appearance88;
			appearance89.TextHAlignAsString = "Left";
			comboBoxConsignExpense.DisplayLayout.Override.HeaderAppearance = appearance89;
			comboBoxConsignExpense.DisplayLayout.Override.HeaderClickAction = Infragistics.Win.UltraWinGrid.HeaderClickAction.SortMulti;
			comboBoxConsignExpense.DisplayLayout.Override.HeaderStyle = Infragistics.Win.HeaderStyle.WindowsXPCommand;
			appearance90.BackColor = System.Drawing.SystemColors.Window;
			appearance90.BorderColor = System.Drawing.Color.Silver;
			comboBoxConsignExpense.DisplayLayout.Override.RowAppearance = appearance90;
			comboBoxConsignExpense.DisplayLayout.Override.RowSelectors = Infragistics.Win.DefaultableBoolean.False;
			appearance91.BackColor = System.Drawing.SystemColors.ControlLight;
			comboBoxConsignExpense.DisplayLayout.Override.TemplateAddRowAppearance = appearance91;
			comboBoxConsignExpense.DisplayLayout.ScrollBounds = Infragistics.Win.UltraWinGrid.ScrollBounds.ScrollToFill;
			comboBoxConsignExpense.DisplayLayout.ScrollStyle = Infragistics.Win.UltraWinGrid.ScrollStyle.Immediate;
			comboBoxConsignExpense.DisplayLayout.ViewStyleBand = Infragistics.Win.UltraWinGrid.ViewStyleBand.OutlookGroupBy;
			comboBoxConsignExpense.DropDownSearchMethod = Infragistics.Win.UltraWinGrid.DropDownSearchMethod.Linear;
			comboBoxConsignExpense.Editable = true;
			comboBoxConsignExpense.ExpenseCodeType = Micromind.Common.Data.ExpenseCodeTypes.ConsignmentIn;
			comboBoxConsignExpense.FilterString = "";
			comboBoxConsignExpense.HasAllAccount = false;
			comboBoxConsignExpense.HasCustom = false;
			comboBoxConsignExpense.IsDataLoaded = false;
			comboBoxConsignExpense.Location = new System.Drawing.Point(575, 216);
			comboBoxConsignExpense.MaxDropDownItems = 12;
			comboBoxConsignExpense.Name = "comboBoxConsignExpense";
			comboBoxConsignExpense.ShowInactiveItems = false;
			comboBoxConsignExpense.ShowQuickAdd = true;
			comboBoxConsignExpense.Size = new System.Drawing.Size(100, 20);
			comboBoxConsignExpense.TabIndex = 133;
			comboBoxConsignExpense.UseFlatMode = Infragistics.Win.DefaultableBoolean.True;
			comboBoxConsignExpense.Visible = false;
			comboBoxConsignIn.Assigned = false;
			comboBoxConsignIn.AutoCompleteMode = Infragistics.Win.AutoCompleteMode.Append;
			comboBoxConsignIn.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper;
			comboBoxConsignIn.CustomReportFieldName = "";
			comboBoxConsignIn.CustomReportKey = "";
			comboBoxConsignIn.CustomReportValueType = 1;
			comboBoxConsignIn.DescriptionTextBox = null;
			appearance92.BackColor = System.Drawing.SystemColors.Window;
			appearance92.BorderColor = System.Drawing.SystemColors.InactiveCaption;
			comboBoxConsignIn.DisplayLayout.Appearance = appearance92;
			comboBoxConsignIn.DisplayLayout.BorderStyle = Infragistics.Win.UIElementBorderStyle.Solid;
			comboBoxConsignIn.DisplayLayout.CaptionVisible = Infragistics.Win.DefaultableBoolean.False;
			appearance93.BackColor = System.Drawing.SystemColors.ActiveBorder;
			appearance93.BackColor2 = System.Drawing.SystemColors.ControlDark;
			appearance93.BackGradientStyle = Infragistics.Win.GradientStyle.Vertical;
			appearance93.BorderColor = System.Drawing.SystemColors.Window;
			comboBoxConsignIn.DisplayLayout.GroupByBox.Appearance = appearance93;
			appearance94.ForeColor = System.Drawing.SystemColors.GrayText;
			comboBoxConsignIn.DisplayLayout.GroupByBox.BandLabelAppearance = appearance94;
			comboBoxConsignIn.DisplayLayout.GroupByBox.BorderStyle = Infragistics.Win.UIElementBorderStyle.Solid;
			appearance95.BackColor = System.Drawing.SystemColors.ControlLightLight;
			appearance95.BackColor2 = System.Drawing.SystemColors.Control;
			appearance95.BackGradientStyle = Infragistics.Win.GradientStyle.Horizontal;
			appearance95.ForeColor = System.Drawing.SystemColors.GrayText;
			comboBoxConsignIn.DisplayLayout.GroupByBox.PromptAppearance = appearance95;
			comboBoxConsignIn.DisplayLayout.MaxColScrollRegions = 1;
			comboBoxConsignIn.DisplayLayout.MaxRowScrollRegions = 1;
			appearance96.BackColor = System.Drawing.SystemColors.Window;
			appearance96.ForeColor = System.Drawing.SystemColors.ControlText;
			comboBoxConsignIn.DisplayLayout.Override.ActiveCellAppearance = appearance96;
			appearance97.BackColor = System.Drawing.SystemColors.Highlight;
			appearance97.ForeColor = System.Drawing.SystemColors.HighlightText;
			comboBoxConsignIn.DisplayLayout.Override.ActiveRowAppearance = appearance97;
			comboBoxConsignIn.DisplayLayout.Override.BorderStyleCell = Infragistics.Win.UIElementBorderStyle.Dotted;
			comboBoxConsignIn.DisplayLayout.Override.BorderStyleRow = Infragistics.Win.UIElementBorderStyle.Dotted;
			appearance98.BackColor = System.Drawing.SystemColors.Window;
			comboBoxConsignIn.DisplayLayout.Override.CardAreaAppearance = appearance98;
			appearance99.BorderColor = System.Drawing.Color.Silver;
			appearance99.TextTrimming = Infragistics.Win.TextTrimming.EllipsisCharacter;
			comboBoxConsignIn.DisplayLayout.Override.CellAppearance = appearance99;
			comboBoxConsignIn.DisplayLayout.Override.CellClickAction = Infragistics.Win.UltraWinGrid.CellClickAction.EditAndSelectText;
			comboBoxConsignIn.DisplayLayout.Override.CellPadding = 0;
			appearance100.BackColor = System.Drawing.SystemColors.Control;
			appearance100.BackColor2 = System.Drawing.SystemColors.ControlDark;
			appearance100.BackGradientAlignment = Infragistics.Win.GradientAlignment.Element;
			appearance100.BackGradientStyle = Infragistics.Win.GradientStyle.Horizontal;
			appearance100.BorderColor = System.Drawing.SystemColors.Window;
			comboBoxConsignIn.DisplayLayout.Override.GroupByRowAppearance = appearance100;
			appearance101.TextHAlignAsString = "Left";
			comboBoxConsignIn.DisplayLayout.Override.HeaderAppearance = appearance101;
			comboBoxConsignIn.DisplayLayout.Override.HeaderClickAction = Infragistics.Win.UltraWinGrid.HeaderClickAction.SortMulti;
			comboBoxConsignIn.DisplayLayout.Override.HeaderStyle = Infragistics.Win.HeaderStyle.WindowsXPCommand;
			appearance102.BackColor = System.Drawing.SystemColors.Window;
			appearance102.BorderColor = System.Drawing.Color.Silver;
			comboBoxConsignIn.DisplayLayout.Override.RowAppearance = appearance102;
			comboBoxConsignIn.DisplayLayout.Override.RowSelectors = Infragistics.Win.DefaultableBoolean.False;
			appearance103.BackColor = System.Drawing.SystemColors.ControlLight;
			comboBoxConsignIn.DisplayLayout.Override.TemplateAddRowAppearance = appearance103;
			comboBoxConsignIn.DisplayLayout.ScrollBounds = Infragistics.Win.UltraWinGrid.ScrollBounds.ScrollToFill;
			comboBoxConsignIn.DisplayLayout.ScrollStyle = Infragistics.Win.UltraWinGrid.ScrollStyle.Immediate;
			comboBoxConsignIn.DisplayLayout.ViewStyleBand = Infragistics.Win.UltraWinGrid.ViewStyleBand.OutlookGroupBy;
			comboBoxConsignIn.DropDownSearchMethod = Infragistics.Win.UltraWinGrid.DropDownSearchMethod.Linear;
			comboBoxConsignIn.Editable = true;
			comboBoxConsignIn.FilterString = "";
			comboBoxConsignIn.HasAllAccount = false;
			comboBoxConsignIn.HasCustom = false;
			comboBoxConsignIn.IsDataLoaded = false;
			comboBoxConsignIn.Location = new System.Drawing.Point(575, 242);
			comboBoxConsignIn.MaxDropDownItems = 12;
			comboBoxConsignIn.Name = "comboBoxConsignIn";
			comboBoxConsignIn.ShowInactiveItems = false;
			comboBoxConsignIn.ShowQuickAdd = true;
			comboBoxConsignIn.Size = new System.Drawing.Size(100, 20);
			comboBoxConsignIn.TabIndex = 134;
			comboBoxConsignIn.UseFlatMode = Infragistics.Win.DefaultableBoolean.True;
			comboBoxConsignIn.Visible = false;
			comboBoxCostCategory.Assigned = false;
			comboBoxCostCategory.AutoCompleteMode = Infragistics.Win.AutoCompleteMode.Append;
			comboBoxCostCategory.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper;
			comboBoxCostCategory.CustomReportFieldName = "";
			comboBoxCostCategory.CustomReportKey = "";
			comboBoxCostCategory.CustomReportValueType = 1;
			comboBoxCostCategory.DescriptionTextBox = null;
			appearance104.BackColor = System.Drawing.SystemColors.Window;
			appearance104.BorderColor = System.Drawing.SystemColors.InactiveCaption;
			comboBoxCostCategory.DisplayLayout.Appearance = appearance104;
			comboBoxCostCategory.DisplayLayout.BorderStyle = Infragistics.Win.UIElementBorderStyle.Solid;
			comboBoxCostCategory.DisplayLayout.CaptionVisible = Infragistics.Win.DefaultableBoolean.False;
			appearance105.BackColor = System.Drawing.SystemColors.ActiveBorder;
			appearance105.BackColor2 = System.Drawing.SystemColors.ControlDark;
			appearance105.BackGradientStyle = Infragistics.Win.GradientStyle.Vertical;
			appearance105.BorderColor = System.Drawing.SystemColors.Window;
			comboBoxCostCategory.DisplayLayout.GroupByBox.Appearance = appearance105;
			appearance106.ForeColor = System.Drawing.SystemColors.GrayText;
			comboBoxCostCategory.DisplayLayout.GroupByBox.BandLabelAppearance = appearance106;
			comboBoxCostCategory.DisplayLayout.GroupByBox.BorderStyle = Infragistics.Win.UIElementBorderStyle.Solid;
			appearance107.BackColor = System.Drawing.SystemColors.ControlLightLight;
			appearance107.BackColor2 = System.Drawing.SystemColors.Control;
			appearance107.BackGradientStyle = Infragistics.Win.GradientStyle.Horizontal;
			appearance107.ForeColor = System.Drawing.SystemColors.GrayText;
			comboBoxCostCategory.DisplayLayout.GroupByBox.PromptAppearance = appearance107;
			comboBoxCostCategory.DisplayLayout.MaxColScrollRegions = 1;
			comboBoxCostCategory.DisplayLayout.MaxRowScrollRegions = 1;
			appearance108.BackColor = System.Drawing.SystemColors.Window;
			appearance108.ForeColor = System.Drawing.SystemColors.ControlText;
			comboBoxCostCategory.DisplayLayout.Override.ActiveCellAppearance = appearance108;
			appearance109.BackColor = System.Drawing.SystemColors.Highlight;
			appearance109.ForeColor = System.Drawing.SystemColors.HighlightText;
			comboBoxCostCategory.DisplayLayout.Override.ActiveRowAppearance = appearance109;
			comboBoxCostCategory.DisplayLayout.Override.BorderStyleCell = Infragistics.Win.UIElementBorderStyle.Dotted;
			comboBoxCostCategory.DisplayLayout.Override.BorderStyleRow = Infragistics.Win.UIElementBorderStyle.Dotted;
			appearance110.BackColor = System.Drawing.SystemColors.Window;
			comboBoxCostCategory.DisplayLayout.Override.CardAreaAppearance = appearance110;
			appearance111.BorderColor = System.Drawing.Color.Silver;
			appearance111.TextTrimming = Infragistics.Win.TextTrimming.EllipsisCharacter;
			comboBoxCostCategory.DisplayLayout.Override.CellAppearance = appearance111;
			comboBoxCostCategory.DisplayLayout.Override.CellClickAction = Infragistics.Win.UltraWinGrid.CellClickAction.EditAndSelectText;
			comboBoxCostCategory.DisplayLayout.Override.CellPadding = 0;
			appearance112.BackColor = System.Drawing.SystemColors.Control;
			appearance112.BackColor2 = System.Drawing.SystemColors.ControlDark;
			appearance112.BackGradientAlignment = Infragistics.Win.GradientAlignment.Element;
			appearance112.BackGradientStyle = Infragistics.Win.GradientStyle.Horizontal;
			appearance112.BorderColor = System.Drawing.SystemColors.Window;
			comboBoxCostCategory.DisplayLayout.Override.GroupByRowAppearance = appearance112;
			appearance113.TextHAlignAsString = "Left";
			comboBoxCostCategory.DisplayLayout.Override.HeaderAppearance = appearance113;
			comboBoxCostCategory.DisplayLayout.Override.HeaderClickAction = Infragistics.Win.UltraWinGrid.HeaderClickAction.SortMulti;
			comboBoxCostCategory.DisplayLayout.Override.HeaderStyle = Infragistics.Win.HeaderStyle.WindowsXPCommand;
			appearance114.BackColor = System.Drawing.SystemColors.Window;
			appearance114.BorderColor = System.Drawing.Color.Silver;
			comboBoxCostCategory.DisplayLayout.Override.RowAppearance = appearance114;
			comboBoxCostCategory.DisplayLayout.Override.RowSelectors = Infragistics.Win.DefaultableBoolean.False;
			appearance115.BackColor = System.Drawing.SystemColors.ControlLight;
			comboBoxCostCategory.DisplayLayout.Override.TemplateAddRowAppearance = appearance115;
			comboBoxCostCategory.DisplayLayout.ScrollBounds = Infragistics.Win.UltraWinGrid.ScrollBounds.ScrollToFill;
			comboBoxCostCategory.DisplayLayout.ScrollStyle = Infragistics.Win.UltraWinGrid.ScrollStyle.Immediate;
			comboBoxCostCategory.DisplayLayout.ViewStyleBand = Infragistics.Win.UltraWinGrid.ViewStyleBand.OutlookGroupBy;
			comboBoxCostCategory.DropDownSearchMethod = Infragistics.Win.UltraWinGrid.DropDownSearchMethod.Linear;
			comboBoxCostCategory.Editable = true;
			comboBoxCostCategory.FilterString = "";
			comboBoxCostCategory.HasAllAccount = false;
			comboBoxCostCategory.HasCustom = false;
			comboBoxCostCategory.IsDataLoaded = false;
			comboBoxCostCategory.Location = new System.Drawing.Point(596, 164);
			comboBoxCostCategory.MaxDropDownItems = 12;
			comboBoxCostCategory.Name = "comboBoxCostCategory";
			comboBoxCostCategory.ShowInactiveItems = false;
			comboBoxCostCategory.ShowQuickAdd = true;
			comboBoxCostCategory.Size = new System.Drawing.Size(79, 20);
			comboBoxCostCategory.TabIndex = 125;
			comboBoxCostCategory.UseFlatMode = Infragistics.Win.DefaultableBoolean.True;
			comboBoxCostCategory.Visible = false;
			comboBoxJob.Assigned = false;
			comboBoxJob.AutoCompleteMode = Infragistics.Win.AutoCompleteMode.Append;
			comboBoxJob.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper;
			comboBoxJob.CustomReportFieldName = "";
			comboBoxJob.CustomReportKey = "";
			comboBoxJob.CustomReportValueType = 1;
			comboBoxJob.DescriptionTextBox = null;
			comboBoxJob.DropDownSearchMethod = Infragistics.Win.UltraWinGrid.DropDownSearchMethod.Linear;
			comboBoxJob.Editable = true;
			comboBoxJob.FilterString = "";
			comboBoxJob.HasAllAccount = false;
			comboBoxJob.HasCustom = false;
			comboBoxJob.IsDataLoaded = false;
			comboBoxJob.Location = new System.Drawing.Point(575, 190);
			comboBoxJob.MaxDropDownItems = 12;
			comboBoxJob.Name = "comboBoxJob";
			comboBoxJob.ShowInactiveItems = false;
			comboBoxJob.ShowQuickAdd = true;
			comboBoxJob.Size = new System.Drawing.Size(100, 20);
			comboBoxJob.TabIndex = 124;
			comboBoxJob.UseFlatMode = Infragistics.Win.DefaultableBoolean.True;
			comboBoxJob.Visible = false;
			comboBoxProperty.Assigned = false;
			comboBoxProperty.AutoCompleteMode = Infragistics.Win.AutoCompleteMode.Append;
			comboBoxProperty.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper;
			comboBoxProperty.CustomReportFieldName = "";
			comboBoxProperty.CustomReportKey = "";
			comboBoxProperty.CustomReportValueType = 1;
			comboBoxProperty.DescriptionTextBox = null;
			appearance116.BackColor = System.Drawing.SystemColors.Window;
			appearance116.BorderColor = System.Drawing.SystemColors.InactiveCaption;
			comboBoxProperty.DisplayLayout.Appearance = appearance116;
			comboBoxProperty.DisplayLayout.BorderStyle = Infragistics.Win.UIElementBorderStyle.Solid;
			comboBoxProperty.DisplayLayout.CaptionVisible = Infragistics.Win.DefaultableBoolean.False;
			appearance117.BackColor = System.Drawing.SystemColors.ActiveBorder;
			appearance117.BackColor2 = System.Drawing.SystemColors.ControlDark;
			appearance117.BackGradientStyle = Infragistics.Win.GradientStyle.Vertical;
			appearance117.BorderColor = System.Drawing.SystemColors.Window;
			comboBoxProperty.DisplayLayout.GroupByBox.Appearance = appearance117;
			appearance118.ForeColor = System.Drawing.SystemColors.GrayText;
			comboBoxProperty.DisplayLayout.GroupByBox.BandLabelAppearance = appearance118;
			comboBoxProperty.DisplayLayout.GroupByBox.BorderStyle = Infragistics.Win.UIElementBorderStyle.Solid;
			appearance119.BackColor = System.Drawing.SystemColors.ControlLightLight;
			appearance119.BackColor2 = System.Drawing.SystemColors.Control;
			appearance119.BackGradientStyle = Infragistics.Win.GradientStyle.Horizontal;
			appearance119.ForeColor = System.Drawing.SystemColors.GrayText;
			comboBoxProperty.DisplayLayout.GroupByBox.PromptAppearance = appearance119;
			comboBoxProperty.DisplayLayout.MaxColScrollRegions = 1;
			comboBoxProperty.DisplayLayout.MaxRowScrollRegions = 1;
			appearance120.BackColor = System.Drawing.SystemColors.Window;
			appearance120.ForeColor = System.Drawing.SystemColors.ControlText;
			comboBoxProperty.DisplayLayout.Override.ActiveCellAppearance = appearance120;
			appearance121.BackColor = System.Drawing.SystemColors.Highlight;
			appearance121.ForeColor = System.Drawing.SystemColors.HighlightText;
			comboBoxProperty.DisplayLayout.Override.ActiveRowAppearance = appearance121;
			comboBoxProperty.DisplayLayout.Override.BorderStyleCell = Infragistics.Win.UIElementBorderStyle.Dotted;
			comboBoxProperty.DisplayLayout.Override.BorderStyleRow = Infragistics.Win.UIElementBorderStyle.Dotted;
			appearance122.BackColor = System.Drawing.SystemColors.Window;
			comboBoxProperty.DisplayLayout.Override.CardAreaAppearance = appearance122;
			appearance123.BorderColor = System.Drawing.Color.Silver;
			appearance123.TextTrimming = Infragistics.Win.TextTrimming.EllipsisCharacter;
			comboBoxProperty.DisplayLayout.Override.CellAppearance = appearance123;
			comboBoxProperty.DisplayLayout.Override.CellClickAction = Infragistics.Win.UltraWinGrid.CellClickAction.EditAndSelectText;
			comboBoxProperty.DisplayLayout.Override.CellPadding = 0;
			appearance124.BackColor = System.Drawing.SystemColors.Control;
			appearance124.BackColor2 = System.Drawing.SystemColors.ControlDark;
			appearance124.BackGradientAlignment = Infragistics.Win.GradientAlignment.Element;
			appearance124.BackGradientStyle = Infragistics.Win.GradientStyle.Horizontal;
			appearance124.BorderColor = System.Drawing.SystemColors.Window;
			comboBoxProperty.DisplayLayout.Override.GroupByRowAppearance = appearance124;
			appearance125.TextHAlignAsString = "Left";
			comboBoxProperty.DisplayLayout.Override.HeaderAppearance = appearance125;
			comboBoxProperty.DisplayLayout.Override.HeaderClickAction = Infragistics.Win.UltraWinGrid.HeaderClickAction.SortMulti;
			comboBoxProperty.DisplayLayout.Override.HeaderStyle = Infragistics.Win.HeaderStyle.WindowsXPCommand;
			appearance126.BackColor = System.Drawing.SystemColors.Window;
			appearance126.BorderColor = System.Drawing.Color.Silver;
			comboBoxProperty.DisplayLayout.Override.RowAppearance = appearance126;
			comboBoxProperty.DisplayLayout.Override.RowSelectors = Infragistics.Win.DefaultableBoolean.False;
			appearance127.BackColor = System.Drawing.SystemColors.ControlLight;
			comboBoxProperty.DisplayLayout.Override.TemplateAddRowAppearance = appearance127;
			comboBoxProperty.DisplayLayout.ScrollBounds = Infragistics.Win.UltraWinGrid.ScrollBounds.ScrollToFill;
			comboBoxProperty.DisplayLayout.ScrollStyle = Infragistics.Win.UltraWinGrid.ScrollStyle.Immediate;
			comboBoxProperty.DisplayLayout.ViewStyleBand = Infragistics.Win.UltraWinGrid.ViewStyleBand.OutlookGroupBy;
			comboBoxProperty.DropDownSearchMethod = Infragistics.Win.UltraWinGrid.DropDownSearchMethod.Linear;
			comboBoxProperty.Editable = true;
			comboBoxProperty.FilterString = "";
			comboBoxProperty.HasAllAccount = false;
			comboBoxProperty.HasCustom = false;
			comboBoxProperty.IsDataLoaded = false;
			comboBoxProperty.Location = new System.Drawing.Point(420, 254);
			comboBoxProperty.MaxDropDownItems = 12;
			comboBoxProperty.Name = "comboBoxProperty";
			comboBoxProperty.ShowInactiveItems = false;
			comboBoxProperty.ShowQuickAdd = true;
			comboBoxProperty.Size = new System.Drawing.Size(176, 20);
			comboBoxProperty.TabIndex = 137;
			comboBoxProperty.UseFlatMode = Infragistics.Win.DefaultableBoolean.True;
			comboBoxProperty.Visible = false;
			comboBoxPropertyUnit.Assigned = false;
			comboBoxPropertyUnit.AutoCompleteMode = Infragistics.Win.AutoCompleteMode.Append;
			comboBoxPropertyUnit.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper;
			comboBoxPropertyUnit.CustomReportFieldName = "";
			comboBoxPropertyUnit.CustomReportKey = "";
			comboBoxPropertyUnit.CustomReportValueType = 1;
			comboBoxPropertyUnit.DescriptionTextBox = null;
			appearance128.BackColor = System.Drawing.SystemColors.Window;
			appearance128.BorderColor = System.Drawing.SystemColors.InactiveCaption;
			comboBoxPropertyUnit.DisplayLayout.Appearance = appearance128;
			comboBoxPropertyUnit.DisplayLayout.BorderStyle = Infragistics.Win.UIElementBorderStyle.Solid;
			comboBoxPropertyUnit.DisplayLayout.CaptionVisible = Infragistics.Win.DefaultableBoolean.False;
			appearance129.BackColor = System.Drawing.SystemColors.ActiveBorder;
			appearance129.BackColor2 = System.Drawing.SystemColors.ControlDark;
			appearance129.BackGradientStyle = Infragistics.Win.GradientStyle.Vertical;
			appearance129.BorderColor = System.Drawing.SystemColors.Window;
			comboBoxPropertyUnit.DisplayLayout.GroupByBox.Appearance = appearance129;
			appearance130.ForeColor = System.Drawing.SystemColors.GrayText;
			comboBoxPropertyUnit.DisplayLayout.GroupByBox.BandLabelAppearance = appearance130;
			comboBoxPropertyUnit.DisplayLayout.GroupByBox.BorderStyle = Infragistics.Win.UIElementBorderStyle.Solid;
			appearance131.BackColor = System.Drawing.SystemColors.ControlLightLight;
			appearance131.BackColor2 = System.Drawing.SystemColors.Control;
			appearance131.BackGradientStyle = Infragistics.Win.GradientStyle.Horizontal;
			appearance131.ForeColor = System.Drawing.SystemColors.GrayText;
			comboBoxPropertyUnit.DisplayLayout.GroupByBox.PromptAppearance = appearance131;
			comboBoxPropertyUnit.DisplayLayout.MaxColScrollRegions = 1;
			comboBoxPropertyUnit.DisplayLayout.MaxRowScrollRegions = 1;
			appearance132.BackColor = System.Drawing.SystemColors.Window;
			appearance132.ForeColor = System.Drawing.SystemColors.ControlText;
			comboBoxPropertyUnit.DisplayLayout.Override.ActiveCellAppearance = appearance132;
			appearance133.BackColor = System.Drawing.SystemColors.Highlight;
			appearance133.ForeColor = System.Drawing.SystemColors.HighlightText;
			comboBoxPropertyUnit.DisplayLayout.Override.ActiveRowAppearance = appearance133;
			comboBoxPropertyUnit.DisplayLayout.Override.BorderStyleCell = Infragistics.Win.UIElementBorderStyle.Dotted;
			comboBoxPropertyUnit.DisplayLayout.Override.BorderStyleRow = Infragistics.Win.UIElementBorderStyle.Dotted;
			appearance134.BackColor = System.Drawing.SystemColors.Window;
			comboBoxPropertyUnit.DisplayLayout.Override.CardAreaAppearance = appearance134;
			appearance135.BorderColor = System.Drawing.Color.Silver;
			appearance135.TextTrimming = Infragistics.Win.TextTrimming.EllipsisCharacter;
			comboBoxPropertyUnit.DisplayLayout.Override.CellAppearance = appearance135;
			comboBoxPropertyUnit.DisplayLayout.Override.CellClickAction = Infragistics.Win.UltraWinGrid.CellClickAction.EditAndSelectText;
			comboBoxPropertyUnit.DisplayLayout.Override.CellPadding = 0;
			appearance136.BackColor = System.Drawing.SystemColors.Control;
			appearance136.BackColor2 = System.Drawing.SystemColors.ControlDark;
			appearance136.BackGradientAlignment = Infragistics.Win.GradientAlignment.Element;
			appearance136.BackGradientStyle = Infragistics.Win.GradientStyle.Horizontal;
			appearance136.BorderColor = System.Drawing.SystemColors.Window;
			comboBoxPropertyUnit.DisplayLayout.Override.GroupByRowAppearance = appearance136;
			appearance137.TextHAlignAsString = "Left";
			comboBoxPropertyUnit.DisplayLayout.Override.HeaderAppearance = appearance137;
			comboBoxPropertyUnit.DisplayLayout.Override.HeaderClickAction = Infragistics.Win.UltraWinGrid.HeaderClickAction.SortMulti;
			comboBoxPropertyUnit.DisplayLayout.Override.HeaderStyle = Infragistics.Win.HeaderStyle.WindowsXPCommand;
			appearance138.BackColor = System.Drawing.SystemColors.Window;
			appearance138.BorderColor = System.Drawing.Color.Silver;
			comboBoxPropertyUnit.DisplayLayout.Override.RowAppearance = appearance138;
			comboBoxPropertyUnit.DisplayLayout.Override.RowSelectors = Infragistics.Win.DefaultableBoolean.False;
			appearance139.BackColor = System.Drawing.SystemColors.ControlLight;
			comboBoxPropertyUnit.DisplayLayout.Override.TemplateAddRowAppearance = appearance139;
			comboBoxPropertyUnit.DisplayLayout.ScrollBounds = Infragistics.Win.UltraWinGrid.ScrollBounds.ScrollToFill;
			comboBoxPropertyUnit.DisplayLayout.ScrollStyle = Infragistics.Win.UltraWinGrid.ScrollStyle.Immediate;
			comboBoxPropertyUnit.DisplayLayout.ViewStyleBand = Infragistics.Win.UltraWinGrid.ViewStyleBand.OutlookGroupBy;
			comboBoxPropertyUnit.DropDownSearchMethod = Infragistics.Win.UltraWinGrid.DropDownSearchMethod.Linear;
			comboBoxPropertyUnit.Editable = true;
			comboBoxPropertyUnit.FilterString = "";
			comboBoxPropertyUnit.HasAllAccount = false;
			comboBoxPropertyUnit.HasCustom = false;
			comboBoxPropertyUnit.IsDataLoaded = false;
			comboBoxPropertyUnit.Location = new System.Drawing.Point(426, 300);
			comboBoxPropertyUnit.MaxDropDownItems = 12;
			comboBoxPropertyUnit.Name = "comboBoxPropertyUnit";
			comboBoxPropertyUnit.ShowActiveOnly = false;
			comboBoxPropertyUnit.ShowInactiveItems = false;
			comboBoxPropertyUnit.ShowQuickAdd = true;
			comboBoxPropertyUnit.Size = new System.Drawing.Size(100, 20);
			comboBoxPropertyUnit.TabIndex = 138;
			comboBoxPropertyUnit.UseFlatMode = Infragistics.Win.DefaultableBoolean.True;
			comboBoxPropertyUnit.Visible = false;
			dateTimePickerGrid.Anchor = System.Windows.Forms.AnchorStyles.Right;
			dateTimePickerGrid.Format = System.Windows.Forms.DateTimePickerFormat.Short;
			dateTimePickerGrid.Location = new System.Drawing.Point(488, 216);
			dateTimePickerGrid.Name = "dateTimePickerGrid";
			dateTimePickerGrid.Size = new System.Drawing.Size(131, 20);
			dateTimePickerGrid.TabIndex = 169;
			dateTimePickerGrid.TabStop = false;
			dateTimePickerGrid.Visible = false;
			base.AutoScaleDimensions = new System.Drawing.SizeF(6f, 13f);
			base.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			BackColor = System.Drawing.Color.WhiteSmoke;
			base.ClientSize = new System.Drawing.Size(702, 516);
			base.Controls.Add(comboBoxPropertyUnit);
			base.Controls.Add(comboBoxProperty);
			base.Controls.Add(labelVoided);
			base.Controls.Add(panelDetails);
			base.Controls.Add(dataGridItems);
			base.Controls.Add(formManager);
			base.Controls.Add(panelButtons);
			base.Controls.Add(ultraGroupBox1);
			base.Controls.Add(comboBoxChequebook);
			base.Controls.Add(comboBoxConsignExpense);
			base.Controls.Add(comboBoxConsignIn);
			base.Controls.Add(comboBoxCostCategory);
			base.Controls.Add(comboBoxJob);
			base.Controls.Add(ultraFormattedLinkLabel6);
			base.Controls.Add(dateTimePickerGrid);
			base.Icon = (System.Drawing.Icon)resources.GetObject("$this.Icon");
			base.KeyPreview = true;
			MinimumSize = new System.Drawing.Size(649, 366);
			base.Name = "ChequePaymentForm";
			Text = "Cheque Payment Voucher";
			base.FormClosing += new System.Windows.Forms.FormClosingEventHandler(AccountGroupDetailsForm_FormClosing);
			panelButtons.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)ultraGroupBox1).EndInit();
			ultraGroupBox1.ResumeLayout(false);
			panelDetails.ResumeLayout(false);
			panelDetails.PerformLayout();
			((System.ComponentModel.ISupportInitialize)comboBoxSysDoc).EndInit();
			((System.ComponentModel.ISupportInitialize)comboBoxCostCenter).EndInit();
			((System.ComponentModel.ISupportInitialize)comboBoxAnalysis).EndInit();
			((System.ComponentModel.ISupportInitialize)dataGridItems).EndInit();
			((System.ComponentModel.ISupportInitialize)comboBoxChequebook).EndInit();
			((System.ComponentModel.ISupportInitialize)comboBoxConsignExpense).EndInit();
			((System.ComponentModel.ISupportInitialize)comboBoxConsignIn).EndInit();
			((System.ComponentModel.ISupportInitialize)comboBoxCostCategory).EndInit();
			((System.ComponentModel.ISupportInitialize)comboBoxJob).EndInit();
			((System.ComponentModel.ISupportInitialize)comboBoxProperty).EndInit();
			((System.ComponentModel.ISupportInitialize)comboBoxPropertyUnit).EndInit();
			ResumeLayout(false);
			PerformLayout();
		}
	}
}
